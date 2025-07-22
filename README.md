# fraud-detection-ml
# 🛡️ Credit Card Fraud Detection

A machine learning pipeline to detect fraudulent credit card transactions using XGBoost. The project includes data preprocessing, model training, and real-time inference API served with FastAPI and Docker.

---

## 📌 Problem Statement

Credit card fraud detection is a binary classification problem with a highly imbalanced dataset. The goal is to detect fraudulent transactions while minimizing false positives.

---

## 📊 Dataset

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Features**: 30 numerical features (`V1`–`V28`, `Amount`, `Time`)
- **Target**: `Class` (0 = Non-Fraud, 1 = Fraud)

---

## 🧱 Project Structure

fraud-detection-ml/
├── README.md
├── requirements.txt
├── Dockerfile
├── data/
├── notebooks/
├── src/
├── app/

- `notebooks/`: Exploratory data analysis and model prototyping
- `src/`: Python scripts for training, evaluation, preprocessing
- `app/`: FastAPI app for serving predictions
- `Dockerfile`: Build containerized inference service

---

## 🔧 Tools & Stack

- **ML & Data**: pandas, numpy, scikit-learn, XGBoost, imbalanced-learn
- **Deployment**: FastAPI, Docker, joblib, Uvicorn

---

## 📈 Model Performance

| Metric     | Value   |
|------------|---------|
| Accuracy   | 0.998   |
| AUC-ROC    | 0.92    |
| Precision  | 0.86    |
| Recall     | 0.82    |

*(Improved using SMOTE + hyperparameter tuning)*

---

## 🚀 Running the API

### 1. Build Docker image
```bash
docker build -t fraud-api .
