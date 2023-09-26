from pydantic import BaseModel


class Location(BaseModel):
    id: int
    lon: str
    lat: str
    herb: str
    added_user: str
