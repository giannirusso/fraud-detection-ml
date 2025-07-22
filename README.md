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
```
### 2. Run container
```bash
docker run -p 8000:8000 fraud-api
```
### 3. Open docs
Visit http://localhost:8000/docs to test the API with Swagger UI.


## 🧪 API Example
POST /predict
```json
{
  "V1": -1.23,
  "V2": 0.45,
  "V3": 2.51,
  "V4": -0.77,
  "Amount": 125.50
}
```
Response:
```json
{
  "fraud": true
}
```
