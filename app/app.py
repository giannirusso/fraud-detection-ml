from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import joblib
import numpy as np

model = joblib.load("app/model.pkl")

app = FastAPI()

model = joblib.load("app/model.pkl")
MODEL_VERSION = "1.0.0"


class FraudInput(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    Amount: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: FraudInput):
    input_df = pd.DataFrame([data.dict()])

    pred = model.predict(input_df)[0]

    prob = None
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_df)
            if proba is not None and len(proba[0]) > 1:
                prob = float(proba[0][1])
    except Exception:
        prob = None

    return {
        "fraud": bool(pred),
        "fraud_probability": prob,
        "model_version": MODEL_VERSION
    }
