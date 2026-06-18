from pydantic import BaseModel

class Forecast(BaseModel):
    event: str
    probability: float
    confidence: float
