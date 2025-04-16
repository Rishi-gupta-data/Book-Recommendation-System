from setuptools import setup, find_packages
<<<<<<< HEAD
=======
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent
>>>>>>> 7b5d19f (Initial commit: Book Recommendation System with collaborative filtering)

setup(
    name="book_recommender",
    version="0.1",
    packages=find_packages(),
<<<<<<< HEAD
=======
    package_dir={"": str(project_root)},
>>>>>>> 7b5d19f (Initial commit: Book Recommendation System with collaborative filtering)
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'scipy',  # Added scipy
        'kaggle',
        'python-dotenv',
        'Flask'  # Added Flask
    ]
)