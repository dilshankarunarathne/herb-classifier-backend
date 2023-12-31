from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.disease_service import get_disease_details, add_disease

"""
    API router for disease endpoint

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        [POST] /api/disease/search
        search_disease: the endpoint for searching a disease

    Raises:
        HTTPException: if the user is not logged in
"""

router = APIRouter(
    prefix="/api/disease",
    tags=["disease"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/insert")
async def insert_disease(
    disease: str = Form(...),
    symptoms: str = Form(...),
    treatment: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for searching a disease

    Args:
       disease (str): the disease to search for
       token (oauth2 bearer token): the token for the user
       symptoms (str): disease symptoms
       treatment (str): treatment for the disease

    Returns:
       (str) Successfully added new disease details record

    Raises:
       HTTPException: if the user is not logged in
    """
    if await get_current_user(token) is None:
        raise credentials_exception

    if add_disease(disease, symptoms, treatment) is True:
        return "successfully added new disease"
    else:
        raise ValueError("disease already exists")


@router.post("/search")
async def search_disease(
    disease: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for searching a disease

    Args:
        disease (str): the disease to search for
        token (oauth2 bearer token): the token for the user

    Returns:
        (str) The disease details

    Raises:
        HTTPException: if the user is not logged in
    """
    if await get_current_user(token) is None:
        raise credentials_exception

    # TODO jsonify the data

    return get_disease_details(disease)
