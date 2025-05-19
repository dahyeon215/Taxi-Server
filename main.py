from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json, os

from app.models import Prediction

app = FastAPI(title="Taxi-Server API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

DATA_PATH = os.getenv("PREDICTION_FILE", "data/latest_preds.json")

@app.post("/predictions")
async def upload(preds: List[Prediction]):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps([p.dict() for p in preds], ensure_ascii=False))
    return {"status":"received","count":len(preds)}

@app.get("/predictions")
async def download():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
