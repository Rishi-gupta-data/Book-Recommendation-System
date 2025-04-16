# 📚 Book Recommendation System

A sophisticated book recommendation engine powered by collaborative filtering techniques (KNN & SVD), featuring an intuitive web interface.

## ✨ Features

- 🤖 **Intelligent Recommendations** using Collaborative Filtering
- 📊 **Similar Books Discovery** via ISBN
- 🌐 **Interactive Web Interface**
- 🔑 **API Endpoints** with Rate Limiting
- 📈 **Performance Metrics** (RMSE, MAE)
- 🔄 **Efficient Data Processing Pipeline**

---

## 🛠️ Tech Stack

| Category           | Tools/Libraries               |
|--------------------|-------------------------------|
| 👨‍💻 **Language**   | Python 3.8+                   |
| ⚙️ **Framework**    | Flask                         |
| 📊 **Data Handling**| Pandas, NumPy, scikit-learn   |
| 🎨 **Frontend**     | HTML, CSS, Font Awesome       |

---

## 📁 Project Structure

📦 **BookRecommendationSystem/**  
│  
├── 📂 **data/**                      # Dataset files  
│   ├── 📝 **raw/**                    # Original unprocessed data  
│   └── 📊 **processed/**              # Cleaned & ready-to-use data  
│  
├── 📂 **frontend/**                  # Web interface  
│   ├── 🎨 **static/**                 # CSS, JS, image assets  
│   └── 📄 **templates/**              # HTML templates (e.g., `index.html`)  
│  
├── 💾 **models/**                    # Trained models (e.g., `SVD.pkl`)  
│  
├── 📓 **notebooks/**                 # Jupyter Notebooks for experimentation  
│  
├── 🔧 **src/**                       # Source code (data processing, recommendation logic)  
│  
└── 📝 **app.py**                     # Main Flask application entry point  

---

## 🚀 How to Run

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:
    ```bash
    python src/webapp/app.py
    ```

3. Open your browser and visit:  
    👉 [http://localhost:5000](http://localhost:5000)
---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

