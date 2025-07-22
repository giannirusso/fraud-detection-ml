from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("app/model.pkl")

app = FastAPI()

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    Amount: float

@app.post("/predict")
def predict(tx: Transaction):
    X = np.array([[tx.V1, tx.V2, tx.V3, tx.V4, tx.Amount]])
    prediction = model.predict(X)
    return {"fraud": bool(prediction[0])}
