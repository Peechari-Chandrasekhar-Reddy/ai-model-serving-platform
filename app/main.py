from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import numpy as np

app = FastAPI(title="AI Model Serving Platform")

MODEL_PATH = "model.pkl"

# Load model
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

class PredictionRequest(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    if not model:
        return {"error": "Model not loaded"}
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
