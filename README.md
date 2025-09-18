# 📚 Book Recommendation System

A sophisticated book recommendation engine powered by collaborative filtering techniques (KNN & SVD), featuring an intuitive web interface.

---

## ✨ Features

- 🤖 **Intelligent Recommendations** using Collaborative Filtering (User-User & Item-Item)
- 📊 **Similar Books Discovery** via ISBN
- 🌐 **Interactive Web Interface** (Flask-based)
- 🔑 **API Endpoints** with Rate Limiting
- 📈 **Performance Metrics** (RMSE, MAE, Precision@K)
- 🔄 **Efficient Data Processing Pipeline**
- 🗂️ **Well-Structured Codebase** for scalability

---

## 🛠️ Tech Stack

| Category           | Tools/Libraries               |
|--------------------|-------------------------------|
| 👨‍💻 **Language**   | Python 3.8+                   |
| ⚙️ **Framework**    | Flask                         |
| 📊 **Data Handling**| Pandas, NumPy, scikit-learn   |
| 📚 **Recommenders** | KNN (Collaborative), SVD (Matrix Factorization) |
| 🎨 **Frontend**     | HTML, CSS, Bootstrap, Font Awesome |

---

## 📁 Project Structure

📦 **BookRecommendationSystem/**  
│  
├── 📂 **data/**                        
│   ├── 📝 **raw/**                   # Original datasets (Books, Ratings, Users)  
│   └── 📊 **processed/**             # Cleaned & preprocessed data  
│  
├── 📂 **frontend/**                  
│   ├── 🎨 **static/**                # CSS, JS, assets  
│   └── 📄 **templates/**             # HTML files (Jinja2 templates)  
│  
├── 💾 **models/**                    # Trained KNN & SVD models  
│  
├── 📓 **notebooks/**                 # Jupyter notebooks for experiments  
│  
├── 🔧 **src/**                       # Core Python modules (ETL, recommenders)  
│  
└── 📝 **app.py**                     # Flask entry point  

---

## 🔄 Workflow Overview

```mermaid
flowchart TD
    A([📝 User Input: Book/ISBN/User ID]):::start --> B{{📊 Data Processing}}
    B --> C[🧹 Clean & Preprocess Data]
    C --> D[📦 Load Models: KNN / SVD]
    D --> E[🤖 Generate Recommendations]
    E --> F[📈 Evaluate with Metrics]
    E --> G[🌐 Render Web Interface]
    G --> H([📚 Display Recommended Books]):::end_node

    classDef start fill:#00b894,stroke:#fff,color:#fff,stroke-width:2px
    classDef process fill:#0984e3,stroke:#fff,color:#fff
    classDef decision fill:#fdcb6e,stroke:#2d3436,color:#2d3436
    classDef analysis fill:#6c5ce7,stroke:#fff,color:#fff
    classDef end_node fill:#d63031,stroke:#fff,color:#fff,stroke-width:2px

    B:::decision
    C:::process
    D:::process
    E:::process
    F:::analysis
    G:::process
````
---
## 🧠 Models Used

### 1️⃣ **KNN (Collaborative Filtering)**

* Uses similarity between users/books based on ratings.
* Finds *nearest neighbors* (similar readers or books).
* Recommends books that similar users liked.

### 2️⃣ **SVD (Matrix Factorization)**

* Decomposes the User-Item rating matrix into latent factors.
* Captures *hidden patterns* in reading behavior.
* Generates **personalized recommendations** even for sparse data.
---

## 📊 Data Pipeline

```mermaid
flowchart LR
    A([📥 Raw Data: Books + Users + Ratings]) --> B[🧹 Preprocessing: Missing Values, Normalization]
    B --> C[🗂️ Train-Test Split]
    C --> D1[🔎 KNN Model Training]
    C --> D2[📐 SVD Model Training]
    D1 --> E[📊 Evaluation]
    D2 --> E
    E --> F([📚 Final Recommendation Engine]):::end_node

%% 🎨 Styling
classDef end_node fill:#d63031,stroke:#fff,color:#fff,stroke-width:2px;
```
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
## 📈 Evaluation Metrics

**RMSE & MAE** → to measure prediction errors.

**Precision@K & Recall@K** → to evaluate recommendation accuracy.

**Hit Rate** → to measure how often recommended books match user preferences.


## 📸 Screenshots


![Screenshot (15)](https://github.com/user-attachments/assets/cb62f845-0272-48eb-8f81-1a8e2b9a2426)


![Screenshot (16)](https://github.com/user-attachments/assets/7e2149a0-eeac-435b-81db-ba71f5458c8a)


![Screenshot (17)](https://github.com/user-attachments/assets/41cc0518-4a36-4145-b309-02e94aec8d62)


![Screenshot (18)](https://github.com/user-attachments/assets/39f259f7-002f-4a2c-9cbc-e5a880b17835)



## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
