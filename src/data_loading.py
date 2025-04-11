import os
from dotenv import load_dotenv
import kaggle
import pandas as pd
import logging
import os
import pandas as pd
from pathlib import Path
from .config import RAW_DATA_DIR, LOGGING_CONFIG

logger = logging.getLogger(__name__)

def configure_kaggle():
    """Configure Kaggle credentials from environment variables."""
    load_dotenv()
    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

def load_kaggle_dataset():
    """Downloads and loads the book recommendation dataset."""
    try:
        configure_kaggle()
        
        # Set up data directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data", "raw")
        os.makedirs(data_dir, exist_ok=True)
        
        # Load the datasets with proper encoding and separator
        users_df = pd.read_csv(os.path.join(data_dir, "BX-Users.csv"), 
                             sep=';', 
                             encoding='latin-1',
                             on_bad_lines='skip')
        
        books_df = pd.read_csv(os.path.join(data_dir, "BX-Books.csv"),
                             sep=';',
                             encoding='latin-1',
                             on_bad_lines='skip')
        
        ratings_df = pd.read_csv(os.path.join(data_dir, "BX-Book-Ratings.csv"),
                               sep=';',
                               encoding='latin-1',
                               on_bad_lines='skip')
        
        if books_df.empty or users_df.empty or ratings_df.empty:
            raise ValueError("One or more datasets are empty")
            
        print("Datasets loaded successfully!")
        return books_df, users_df, ratings_df
        
    except Exception as e:
        print(f"Error in data loading: {str(e)}")
        return None, None, None

def get_project_root():
    """Returns the absolute path to the project root directory."""
    return Path(__file__).parent.parent

def load_dataset(data_dir="data/raw"):
    """Loads the book recommendation dataset from local CSV files."""
    try:
        root_dir = get_project_root()
        data_path = root_dir / data_dir

        dataset_files = {
            "BX-Users.csv": ["User-ID", "Location", "Age"],
            "BX-Books.csv": ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", 
                            "Publisher", "Image-URL-S", "Image-URL-M", "Image-URL-L"],
            "BX-Book-Ratings.csv": ["User-ID", "ISBN", "Book-Rating"]
        }

        dataframes = {}
        
        for file_name, expected_columns in dataset_files.items():
            file_path = data_path / file_name
            
            if not file_path.exists():
                raise FileNotFoundError(f"Required file not found: {file_path}")
                
            df = pd.read_csv(
                file_path,
                sep=';',
                encoding='latin-1',
                on_bad_lines='skip',
                low_memory=False
            )
            
            missing_cols = [col for col in expected_columns if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns in {file_name}: {missing_cols}")
                
            dataframes[file_name.split('.')[0]] = df

        return (dataframes["BX-Books"], 
                dataframes["BX-Users"], 
                dataframes["BX-Book-Ratings"])

    except Exception as e:
        print(f"Error during data loading: {str(e)}")
        return None, None, None

def ensure_raw_data(dataset_slug="arashnic/book-recommendation-dataset", destination_dir=RAW_DATA_DIR):
    """Checks for raw data files, downloads from Kaggle if missing."""
    destination_dir = Path(destination_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)

    expected_files = ["BX-Users.csv", "BX-Books.csv", "BX-Book-Ratings.csv"]
    files_exist = all((destination_dir / f).exists() for f in expected_files)

    if files_exist:
        logger.info("Raw data files already exist")
        return True

    logger.info("Raw data files not found. Attempting download from Kaggle...")
    try:
        kaggle.api.dataset_download_files(
            dataset_slug, 
            path=destination_dir, 
            unzip=True,
            quiet=False
        )
        logger.info("Download complete")
        return all((destination_dir / f).exists() for f in expected_files)
    except Exception as e:
        logger.error(f"Error downloading data: {e}")
        return False

def load_raw_data_from_files(data_dir=RAW_DATA_DIR):
    """Loads the raw book recommendation dataset from local CSV files."""
    try:
        users_file = data_dir / "BX-Users.csv"
        books_file = data_dir / "BX-Books.csv"
        ratings_file = data_dir / "BX-Book-Ratings.csv"

        if not all(f.exists() for f in [users_file, books_file, ratings_file]):
            raise FileNotFoundError("One or more data files missing")

        users_df = pd.read_csv(users_file, sep=';', encoding='latin-1', on_bad_lines='skip')
        books_df = pd.read_csv(books_file, sep=';', encoding='latin-1', on_bad_lines='skip')
        ratings_df = pd.read_csv(ratings_file, sep=';', encoding='latin-1', on_bad_lines='skip')

        return books_df, users_df, ratings_df

    except Exception as e:
        logger.error(f"Error loading raw data: {e}")
        return None, None, None

if __name__ == "__main__":
    logging.config.dictConfig(LOGGING_CONFIG)
    
    if ensure_raw_data():
        books, users, ratings = load_raw_data_from_files()
        if all(df is not None for df in [books, users, ratings]):
            logger.info("Data loaded successfully")
            logger.info(f"Books shape: {books.shape}")
            logger.info(f"Users shape: {users.shape}")
            logger.info(f"Ratings shape: {ratings.shape}")
        else:
            logger.error("Failed to load data")
    else:
        logger.error("Failed to ensure raw data presence")