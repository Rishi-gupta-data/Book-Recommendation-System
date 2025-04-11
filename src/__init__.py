"""Book Recommendation System package."""

from .config import (
    DATA_CONFIG,
    SVD_PARAMS,
    DATA_PROCESSING,
    LOGGING_CONFIG,
    BASE_DIR,
    DATA_DIR,
    MODEL_DIR
)
from .data_loading import load_dataset
from .data_processing import preprocess_data
from .evaluation import evaluate_recommendations, evaluate_svd_model

__all__ = [
    'load_dataset',
    'preprocess_data',
    'evaluate_recommendations',
    'evaluate_svd_model',
    'DATA_CONFIG',
    'SVD_PARAMS',
    'DATA_PROCESSING',
    'LOGGING_CONFIG',
    'BASE_DIR',
    'DATA_DIR',
    'MODEL_DIR'
]