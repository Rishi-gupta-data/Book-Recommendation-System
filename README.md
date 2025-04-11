# 📚 Book Recommendation System

This project implements a **Book Recommendation System** using collaborative filtering techniques (KNN & SVD) and is served via a Flask-based web interface.

## ✨ Features

- 🤖 Collaborative Filtering (KNN + SVD)
- 📈 Evaluation: RMSE, MAE, Precision/Recall
- 🌐 Flask Web Interface
- 🔌 Optional REST API

## 📁 Project Structure

```
📚 BookRecommendationSystem/
├── 📂 data/                         # Dataset directory
│   ├── 📂 raw/                      # Original raw data files
│   └── 📂 processed/                # Cleaned/preprocessed datasets
│
├── 🪵 logs/                         # Logs for training/debugging
│
├── 📦 models/                       # Trained model artifacts
│   └── 📄 latest_model.pkl          # Final SVD model file
│
├── 🧠 src/                          # Core application code
│   ├── 🧾 __init__.py
│   ├── ⚙️ config.py                 # Global config and parameters
│   ├── 📥 data_loading.py           # Data ingestion utilities
│   ├── 🧹 data_processing.py        # Preprocessing pipeline
│   ├── 📈 evaluation.py             # Evaluation metrics (RMSE, MAE)
│   ├── 🧠 recommender.py            # Model training & recommendation logic
│   └── 🌐 webapp/                   # Web app interface (Flask)
│       ├── 🚀 app.py                # Flask app entrypoint
│       ├── 🧩 models_app.py         # (Optional) API routes
│       ├── 🖼 templates/
│       │   └── 📝 index.html        # HTML frontend
│       └── 🎨 static/               # CSS, JS, images (if any)
│
├── 🔐 .env                          # Environment variables (excluded from Git)
├── 🚫 .gitignore                   # Files to ignore in version control
├── ⚙️ Procfile                      # Render deployment config
├── 📘 README.md                     # Project documentation
├── 📦 requirements.txt              # Python dependencies
└── 📦 setup.py                      # (Optional) installable packaging script
```

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/webapp/app.py
```

Then visit 👉 http://localhost:5000
