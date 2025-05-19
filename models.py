from pydantic import BaseModel

class Prediction(BaseModel):
    latitude: float
    longitude: float
    demand: float
