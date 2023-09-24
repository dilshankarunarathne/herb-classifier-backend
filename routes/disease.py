from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.disease_service import get_disease_details

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


@router.post("/search")
async def search_disease(
    disease: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for searching a disease
    :param disease: the disease to search for
    :param token: the token of the user
    :return: the disease details
    :raises HTTPException: if the user is not logged in
    """
    if get_current_user(token) is None:
        raise credentials_exception

    # TODO jsonify the data

    return get_disease_details(disease)
