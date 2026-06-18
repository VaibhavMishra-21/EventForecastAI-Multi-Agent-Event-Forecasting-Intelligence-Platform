from pydantic import BaseModel

class Event(BaseModel):
    title: str
    country: str
    category: str
    description: str
