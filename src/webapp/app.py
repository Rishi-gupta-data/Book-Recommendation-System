from flask import Flask, render_template, request, jsonify
import pandas as pd
import logging
from pathlib import Path
from functools import wraps
from time import time
from src.recommender import BookRecommender
from src.config import PROCESSED_DATA_DIR, MODEL_DIR, LOGGING_CONFIG, SVD_PARAMS
from src.data_processing import load_processed_data

# Set up logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Rate limiting decorator
def rate_limit(limit=30, window=60):  # 30 requests per minute
    def decorator(f):
        requests = {}
        @wraps(f)
        def wrapped(*args, **kwargs):
            now = time()
            request_id = request.remote_addr
            if request_id not in requests:
                requests[request_id] = []
            requests[request_id] = [t for t in requests[request_id] if t > now - window]
            if len(requests[request_id]) >= limit:
                return jsonify({"error": "Rate limit exceeded"}), 429
            requests[request_id].append(now)
            return f(*args, **kwargs)
        return wrapped
    return decorator

app = Flask(__name__)

# Load processed data with proper error handling
logger.info("Loading processed data...")
books, users, ratings = load_processed_data()
if any(df is None for df in [books, users, ratings]):
    error_msg = "Failed to load required data files. Please ensure data preprocessing is complete."
    logger.error(error_msg)
    raise RuntimeError(error_msg)
logger.info("Processed data loaded successfully")

# Initialize recommender
logger.info("Initializing recommender...")
model_path = MODEL_DIR / "latest_model.pkl"
if not model_path.exists():
    error_msg = (
        f"Model file not found: {model_path}\n"
        "Please ensure:\n"
        "1. The model has been trained\n"
        "2. The model file has been copied to the models directory\n"
        "3. The file is named 'latest_model.pkl'"
    )
    logger.error(error_msg)
    raise FileNotFoundError(error_msg)

recommender = BookRecommender(model_path)
if not recommender.load_model():
    error_msg = (
        f"Failed to load model from {model_path}.\n"
        "This could be due to:\n"
        "1. File corruption\n"
        "2. Insufficient permissions\n"
        "3. Incompatible model format"
    )
    logger.error(error_msg)
    raise RuntimeError(error_msg)

logger.info("Model loaded successfully")

# Get sample of valid users for demonstration
try:
    user_ratings_count = ratings.groupby('User-ID').size()
    active_users = user_ratings_count[user_ratings_count > 5].index.tolist()[:20]
except Exception as e:
    logger.error(f"Error preparing active users list: {e}")
    raise RuntimeError("Failed to prepare active users list")

@app.route("/", methods=["GET", "POST"])
@rate_limit()
def index():
    """Handle main page requests."""
    recommendations = None
    similar_books = None
    error = None
    
    try:
        if request.method == "POST":
            if "user_id" in request.form:
                try:
                    user_id = int(request.form["user_id"])
                    if user_id not in active_users:
                        error = f"Invalid user ID. Please choose from: {active_users[:5]}"
                    else:
                        recommendations = recommender.get_recommendations(
                            user_id, 
                            books,
                            n_recommendations=SVD_PARAMS['default_recommendations']
                        )
                        if not recommendations:
                            error = f"No recommendations found for User {user_id}"
                except ValueError:
                    error = "Please enter a valid numeric user ID"
                    
            elif "isbn" in request.form:
                isbn = request.form["isbn"].strip()
                if not isbn:
                    error = "Please enter a valid ISBN"
                else:
                    similar_books = recommender.get_similar_books(isbn, books)
                    if not similar_books:
                        error = f"No similar books found for ISBN {isbn}"
            
    except Exception as e:
        logger.exception("Unexpected error in index route")
        error = "An unexpected error occurred. Please try again later."
    
    return render_template(
        "index.html", 
        recommendations=recommendations,
        similar_books=similar_books,
        error=error,
        valid_users=active_users
    )

@app.route("/api/users", methods=["GET"])
@rate_limit()
def get_users():
    """API endpoint to get valid user IDs."""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        
        paginated_users = active_users[start_idx:end_idx]
        
        return jsonify({
            "users": paginated_users,
            "total": len(active_users),
            "page": page,
            "per_page": per_page,
            "total_pages": (len(active_users) + per_page - 1) // per_page
        })
    except Exception as e:
        logger.exception("Error in get_users endpoint")
        return jsonify({"error": str(e)}), 500

@app.route("/api/books/<isbn>/similar", methods=["GET"])
@rate_limit()
def get_similar_books_api(isbn):
    """API endpoint to get similar books."""
    try:
        limit = request.args.get('limit', SVD_PARAMS['default_recommendations'], type=int)
        similar_books = recommender.get_similar_books(isbn, books, n_recommendations=limit)
        
        if not similar_books:
            return jsonify({"error": f"No similar books found for ISBN {isbn}"}), 404
            
        return jsonify({"similar_books": similar_books})
    except Exception as e:
        logger.exception(f"Error getting similar books for ISBN {isbn}")
        return jsonify({"error": str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.exception("Internal server error")
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=False)  # Set to False in production