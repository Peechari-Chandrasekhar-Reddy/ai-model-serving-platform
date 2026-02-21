import logging
import joblib
from fastapi import FastAPI, Request
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Model Serving Platform")

# Load trained model
model = joblib.load("model.pkl")

# Request schema
class PredictionRequest(BaseModel):
    features: list[float]

# Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Health endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = model.predict([request.features])
    return {"prediction": prediction.tolist()}

# Expose Prometheus metrics
Instrumentator().instrument(app).expose(app)
