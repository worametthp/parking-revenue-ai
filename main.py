from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import uvicorn
import os

app = FastAPI(title="Parking Revenue AI API")

# Load model and mapping
MODEL_PATH = "models/parking_model.pkl"
MAPPING_PATH = "models/parking_mapping.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    parking_mapping = joblib.load(MAPPING_PATH)
else:
    model = None

class PredictionInput(BaseModel):
    park_name: str = Field(..., example="Bangkok Noi")
    day_of_week: int = Field(..., ge=0, le=6)
    month: int = Field(..., ge=1, le=12)
    is_weekend: int = Field(..., ge=0, le=1)
    rev_lag_1: float = Field(..., description="Revenue from yesterday")
    rev_lag_7: float = Field(..., description="Revenue from same day last week")
    rev_rolling_7: float = Field(..., description="7-day average revenue")

@app.post("/predict")
async def predict(data: PredictionInput):
    if not model:
        raise HTTPException(status_code=500, detail="Model not found. Please train the model first.")
    
    # Map name to ID
    inv_map = {v: k for k, v in parking_mapping.items()}
    park_id = inv_map.get(data.park_name)
    
    if park_id is None:
        raise HTTPException(status_code=404, detail="Parking location not found")

    # Create DataFrame for prediction
    input_df = pd.DataFrame([{
        'park_id': park_id,
        'day_of_week': data.day_of_week,
        'month': data.month,
        'is_weekend': data.is_weekend,
        'rev_lag_1': data.rev_lag_1,
        'rev_lag_7': data.rev_lag_7,
        'rev_rolling_7': data.rev_rolling_7
    }])

    prediction = model.predict(input_df)[0]
    
    return {
        "status": "success",
        "park_name": data.park_name,
        "predicted_revenue": round(float(prediction), 2),
        "currency": "THB"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)