from pydantic import BaseModel

class Herb(BaseModel):
    id: int
    disease: str
    herb: str
