from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.disease_service import get_disease_details, add_disease
from services.es_service import diagnose_by_disease

"""
    API router for esystem (expert system) endpoint

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        

    Raises:
        HTTPException: if the user is not logged in
"""

router = APIRouter(
    prefix="/api/esystem",
    tags=["esystem"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/")
async def search_disease(
    disease: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    return diagnose_by_disease(disease)
