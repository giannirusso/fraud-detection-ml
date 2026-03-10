from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import joblib
import numpy as np

model = joblib.load("app/model.pkl")

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/health")
def health():
    return {"status": "ok"}

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    Amount: float

@app.post("/predict")
def predict(data: FraudInput):
    input_df = pd.DataFrame([data.dict()])

    pred = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(input_df)[0][1])
    else:
        prob = None

    return {
        "fraud": bool(pred),
        "fraud_probability": prob,
        "model_version": MODEL_VERSION
    }
