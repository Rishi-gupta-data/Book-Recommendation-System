# Book Recommendation System

## Overview
This project implements a **Book Recommendation System** using collaborative filtering techniques. The system uses two approaches: **K-Nearest Neighbors (KNN)** and **Singular Value Decomposition (SVD)** to recommend books to users based on their ratings.

The system aims to help users find books that align with their preferences by leveraging historical data of book ratings and similarities between users and books.

## Features
- **Collaborative Filtering**: Both KNN and SVD algorithms are implemented to generate book recommendations
- **User-Based Recommendations**: Users can input a book they like, and the system will recommend other similar books
- **Web Interface**: Easy-to-use Flask web application for interacting with the system
- **RESTful API**: Endpoints for programmatic access to recommendations
- **Evaluation Metrics**: Precision, recall, and hit rate metrics for system evaluation

## Project Structure

BookRecommendationSystem/
├── data/
│   ├── processed/      # Cleaned books, ratings, users CSVs
│   └── raw/           # Original raw datasets (optional)
├── logs/              # Log files (optional)
├── models/
│   └── latest_model.pkl  # Trained SVD model file
├── src/
│   ├── config.py      # Configuration settings
│   ├── data_loading.py    # Data loading utilities
│   ├── data_processing.py # Data preprocessing
│   ├── evaluation.py      # Model evaluation
│   ├── recommender.py     # Core recommendation logic
│   └── webapp/
│       ├── app.py         # Flask app entry point
│       ├── templates/     # HTML templates
│       └── static/        # CSS/JS assets
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation

## 🧠 How It Works

1. **Data Preprocessing**
   - Clean and normalize raw user/book/rating data
   - Build a sparse user-item matrix
   - Handle missing values and outliers

2. **Model Training**
   - Train SVD model using Stochastic Gradient Descent
   - Store the learned user (`U`) and item (`V`) matrices
   - Optimize for minimal prediction error

3. **Recommendation Generation**
   - Calculate predictions using `U × Vᵀ`
   - Generate top N recommendations per user
   - Find similar books using learned features

## 🛠 Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd BookRecommendationSystem