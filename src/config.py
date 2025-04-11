from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODEL_DIR = BASE_DIR / "models"
LOG_DIR = BASE_DIR / "logs"

# Data configuration
DATA_CONFIG = {
    'books': {
        'ISBN': 'ISBN',
        'title': 'Book-Title',
        'author': 'Book-Author',
        'year': 'Year-Of-Publication',
        'publisher': 'Publisher'
    },
    'users': {
        'user_id': 'User-ID',
        'location': 'Location',
        'age': 'Age'
    },
    'ratings': {
        'user_id': 'User-ID',
        'ISBN': 'ISBN',
        'rating': 'Book-Rating'
    }
}

# Model parameters
SVD_PARAMS = {
    "n_factors": 50,
    "n_epochs": 20,
    "learning_rate": 0.005,
    "regularization": 0.02,
    "default_recommendations": 10,
    "min_rating_threshold": 3.0
}

# Data processing parameters
DATA_PROCESSING = {
    'min_book_ratings': 5,
    'min_user_ratings': 3,
    'test_size': 0.2,
    'validation_size': 0.1,
    'random_state': 42
}

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': str(LOG_DIR / 'app.log'),
            'formatter': 'standard',
            'level': 'INFO'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# Create necessary directories
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR, LOG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)