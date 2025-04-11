from setuptools import setup, find_packages

setup(
    name="book_recommender",
    version="0.1",
    packages=find_packages(),
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