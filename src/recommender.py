import pickle
import numpy as np
import logging
import logging.config
from pathlib import Path
<<<<<<< HEAD
=======
import json
>>>>>>> 7b5d19f (Initial commit: Book Recommendation System with collaborative filtering)
from typing import List, Dict, Optional, Union
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .config import SVD_PARAMS, MODEL_DIR, LOGGING_CONFIG, DATA_CONFIG

# Set up logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

class BookRecommender:
    def __init__(self, model_path: Optional[Union[str, Path]] = None):
        """Initialize the recommender system."""
<<<<<<< HEAD
        self.model_path = Path(model_path) if model_path else MODEL_DIR / "latest_model.pkl"
=======
        if model_path:
            self.model_path = Path(model_path)
        else:
            self.model_path = Path(__file__).parent.parent / "models" / "latest_model.pkl"
>>>>>>> 7b5d19f (Initial commit: Book Recommendation System with collaborative filtering)
        self.U = None
        self.Vt = None
        self.user_mapping = None
        self.item_mapping = None

    def load_model(self) -> bool:
        try:
            logger.info(f"Checking if model file exists at: {self.model_path}")
            if not self.model_path.exists():
                logger.error(f"Model file not found: {self.model_path}")
                return False
                
            logger.info(f"Model file size: {self.model_path.stat().st_size} bytes")
            with open(self.model_path, 'rb') as f:
                try:
                    model_info = pickle.load(f)
                    logger.info("Successfully loaded pickle data")
                except pickle.UnpicklingError as pe:
                    logger.error(f"Failed to unpickle model data: {str(pe)}")
                    logger.error("The model file might be corrupted")
                    return False
                except EOFError:
                    logger.error("Model file is empty or truncated")
                    return False

            # Check model structure
            required_keys = ["U", "Vt", "user_mapping", "item_mapping"]
            missing_keys = [key for key in required_keys if key not in model_info]
            if missing_keys:
                logger.error(f"Model file is missing required keys: {missing_keys}")
                return False

            logger.info("Assigning model components...")
            self.U = model_info['U']
            self.Vt = model_info['Vt']
            self.user_mapping = model_info['user_mapping']
            self.item_mapping = model_info['item_mapping']
            
            logger.info(f"Model loaded successfully from {self.model_path}")
            return True
            
        except PermissionError:
            logger.error(f"Permission denied accessing model file: {self.model_path}")
            return False
        except Exception as e:
            logger.exception(f"Unexpected error loading model: {str(e)}")
            return False

<<<<<<< HEAD
=======
    def load_from_portable(self, directory: Union[str, Path]) -> bool:
        """Load model from portable format (numpy arrays and JSON files)."""
        try:
            directory = Path(directory)
            logger.info(f"Loading portable model from: {directory}")

            self.U = np.load(directory / "U.npy")
            self.Vt = np.load(directory / "Vt.npy")

            with open(directory / "user_mapping.json", "r") as f:
                self.user_mapping = {int(k): v for k, v in json.load(f).items()}
            with open(directory / "item_mapping.json", "r") as f:
                self.item_mapping = json.load(f)

            logger.info("✅ Portable model loaded successfully")
            return True
        except Exception as e:
            logger.exception("❌ Failed to load from portable model")
            return False

>>>>>>> 7b5d19f (Initial commit: Book Recommendation System with collaborative filtering)
    def get_recommendations(
        self,
        user_id: int,
        books_df: pd.DataFrame,
        n_recommendations: int = SVD_PARAMS['default_recommendations'],
        min_rating_threshold: float = SVD_PARAMS['min_rating_threshold']
    ) -> List[Dict]:
        try:
            if self.U is None or self.Vt is None:
                if not self.load_model():
                    logger.error("Cannot get recommendations: Model not loaded.")
                    return []
            
            if user_id not in self.user_mapping:
                logger.warning(f"User ID {user_id} not found in training data")
                return []
            
            user_idx = self.user_mapping[user_id]
            
            # Calculate predictions for this user only
            user_predictions = np.dot(self.U[user_idx, :], self.Vt)
            
            # Get top N recommendations
            top_n_idx = np.argsort(user_predictions)[::-1]
            
            recommendations = []
            reverse_item_mapping = {v: k for k, v in self.item_mapping.items()}
            books_df_indexed = books_df.set_index('ISBN')
            
            processed_items = 0
            for idx in top_n_idx:
                processed_items += 1
                if processed_items > len(self.item_mapping) * 0.1 and len(recommendations) < n_recommendations / 2:
                    break
                if len(recommendations) >= n_recommendations:
                    break

                predicted_rating = user_predictions[idx]
                if predicted_rating < min_rating_threshold:
                    continue
                    
                try:
                    isbn = reverse_item_mapping[idx]
                    book_info = books_df_indexed.loc[isbn]
                    
                    recommendations.append({
                        'isbn': isbn,
                        'title': book_info['Book-Title'],
                        'author': book_info['Book-Author'],
                        'predicted_rating': float(predicted_rating),
                        'year': book_info['Year-Of-Publication'],
                        'publisher': book_info['Publisher']
                    })
                except KeyError:
                    logger.warning(f"ISBN {isbn} not found in books dataframe")
                    continue
            
            return recommendations
            
        except Exception as e:
            logger.exception(f"Error getting recommendations for user {user_id}: {str(e)}")
            return []

    def get_similar_books(
        self,
        isbn: str,
        books_df: pd.DataFrame,
        n_recommendations: int = SVD_PARAMS['default_recommendations']
    ) -> List[Dict]:
        try:
            if self.U is None or self.Vt is None:
                if not self.load_model():
                    logger.error("Cannot get similar books: Model not loaded.")
                    return []
            
            if isbn not in self.item_mapping:
                logger.warning(f"ISBN {isbn} not found in training data")
                return []
            
            item_idx = self.item_mapping[isbn]
            target_vector = self.Vt[:, item_idx].reshape(1, -1)
            
            # Calculate cosine similarity
            similarities = cosine_similarity(target_vector, self.Vt.T).flatten()
            
            # Get top N similar books
            similar_idx = np.argsort(similarities)[::-1][1:n_recommendations+1]
            
            similar_books = []
            reverse_item_mapping = {v: k for k, v in self.item_mapping.items()}
            books_df_indexed = books_df.set_index('ISBN')
            
            for idx in similar_idx:
                try:
                    similar_isbn = reverse_item_mapping[idx]
                    book_info = books_df_indexed.loc[similar_isbn]
                    
                    similar_books.append({
                        'isbn': similar_isbn,
                        'title': book_info['Book-Title'],
                        'author': book_info['Book-Author'],
                        'similarity_score': float(similarities[idx]),
                        'year': book_info['Year-Of-Publication'],
                        'publisher': book_info['Publisher']
                    })
                except KeyError:
                    logger.warning(f"Similar ISBN {similar_isbn} not found in books dataframe")
                    continue
            
            return similar_books
            
        except Exception as e:
            logger.exception(f"Error finding similar books for ISBN {isbn}: {str(e)}")
            return []

if __name__ == "__main__":
    from data_loading import load_dataset
    
    recommender = BookRecommender()
    books, users, ratings = load_dataset()
    
    if all(data is not None for data in [books, users, ratings]):
        # Test user recommendations
        test_user_id = users[DATA_CONFIG['users']['user_id']].iloc[0]
        recommendations = recommender.get_recommendations(test_user_id, books)
        
        if recommendations:
            print("\nRecommended books:")
            for rec in recommendations:
                print(f"- {rec['title']} by {rec['author']} "
                      f"(predicted rating: {rec['predicted_rating']:.2f})")
        
        # Test similar books
        test_isbn = books[DATA_CONFIG['books']['ISBN']].iloc[0]
        similar_books = recommender.get_similar_books(test_isbn, books)
        
        if similar_books:
            print("\nSimilar books:")
            for book in similar_books:
                print(f"- {book['title']} by {book['author']} "
                      f"(similarity: {book['similarity_score']:.2f})")