from pydantic import BaseModel


class Disease(BaseModel):
    id: int
    disease: str
    symptoms: str
    treatment
