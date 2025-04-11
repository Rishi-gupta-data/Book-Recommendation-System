import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_recommendations(test_ratings, predictions, k=5):
    """
    Evaluate the recommendation model using various metrics.
    
    Args:
        test_ratings: Actual ratings from test set
        predictions: Predicted ratings
        k: Number of recommendations to consider
    
    Returns:
        dict: Dictionary containing various evaluation metrics
    """
    metrics = {
        'rmse': np.sqrt(mean_squared_error(test_ratings, predictions)),
        'mae': mean_absolute_error(test_ratings, predictions),
        'precision_at_k': calculate_precision_at_k(test_ratings, predictions, k),
        'recall_at_k': calculate_recall_at_k(test_ratings, predictions, k)
    }
    return metrics

def calculate_precision_at_k(actual, predicted, k):
    """Calculate precision@k for recommendations"""
    # Get top k predictions
    top_k_pred = np.argsort(predicted)[:, -k:]
    
    # Create mask for actual positive ratings (ratings > threshold)
    actual_positive = actual > actual.mean()
    
    # Calculate precision for each user
    precisions = []
    for user_idx in range(len(actual)):
        if np.sum(actual_positive[user_idx]) > 0:
            pred_set = set(top_k_pred[user_idx])
            actual_set = set(np.where(actual_positive[user_idx])[0])
            precisions.append(len(pred_set & actual_set) / k)
    
    return np.mean(precisions) if precisions else 0.0

def calculate_recall_at_k(actual, predicted, k):
    """Calculate recall@k for recommendations"""
    # Get top k predictions
    top_k_pred = np.argsort(predicted)[:, -k:]
    
    # Create mask for actual positive ratings
    actual_positive = actual > actual.mean()
    
    # Calculate recall for each user
    recalls = []
    for user_idx in range(len(actual)):
        n_relevant = np.sum(actual_positive[user_idx])
        if n_relevant > 0:
            pred_set = set(top_k_pred[user_idx])
            actual_set = set(np.where(actual_positive[user_idx])[0])
            recalls.append(len(pred_set & actual_set) / n_relevant)
    
    return np.mean(recalls) if recalls else 0.0

def evaluate_svd_model(actual_ratings, predicted_ratings):
    """
    Evaluate SVD model performance
    
    Args:
        actual_ratings: Original ratings matrix
        predicted_ratings: Predicted ratings matrix
    
    Returns:
        dict: Dictionary of evaluation metrics
    """
    mask = actual_ratings != 0
    
    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(
        actual_ratings[mask], 
        predicted_ratings[mask]
    ))
    
    # Calculate MAE
    mae = np.mean(np.abs(
        actual_ratings[mask] - predicted_ratings[mask]
    ))
    
    return {
        'rmse': rmse,
        'mae': mae
    }