import os
import shutil
import logging
import logging.config
from pathlib import Path
from datetime import datetime
from src.config import MODEL_DIR, LOGGING_CONFIG

# Set up logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def update_latest_model():
    """
    Updates the latest_model.pkl by copying the most recent model file.
    Returns True if successful, False otherwise.
    """
    try:
        # Use the specific model file
        source_model = MODEL_DIR / "svd_model_20250409_125709.pkl"
        
        if not source_model.exists():
            logger.error(f"Source model file not found: {source_model}")
            return False
            
        latest_symlink = MODEL_DIR / "latest_model.pkl"
        
        # Remove existing symlink/file if it exists
        if latest_symlink.exists():
            latest_symlink.unlink()
            
        # Copy the model
        shutil.copy2(source_model, latest_symlink)
        logger.info(f"Successfully copied {source_model.name} to latest_model.pkl")
        return True
        
    except Exception as e:
        logger.error(f"Error updating latest model: {e}")
        return False

if __name__ == "__main__":
    if update_latest_model():
        print("✅ Latest model updated successfully")
    else:
        print("❌ Failed to update latest model")