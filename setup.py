from setuptools import setup, find_packages
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent

setup(
    name="book_recommender",
    version="0.1",
    packages=find_packages(),
    package_dir={"": str(project_root)},
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