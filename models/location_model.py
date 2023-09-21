from pydantic import BaseModel


class Location(BaseModel):
    id: int
    lon: float
    lat: float
    herb: str
