# Models Directory

This directory stores trained recommendation models and related files.

## Model Files
- svd_model_latest.pkl: Latest trained SVD model
- svd_model_YYYYMMDD_HHMMSS.pkl: Versioned SVD models with timestamps

## Model Format
SVD model files contain:
- U: User latent factors matrix
- Vt: Transposed item latent factors matrix
- user_mapping: Dictionary mapping user IDs to matrix indices
- item_mapping: Dictionary mapping ISBN to matrix indices
- params: Training parameters used

## Usage
The latest model is automatically loaded by the recommender system. 
Historical models are kept for comparison and fallback.