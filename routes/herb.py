from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.herb_service import get_herb_by_disease, get_disease_by_herb

"""
    API router for herb endpoint

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        

    Raises:
        HTTPException: if the user is not logged in
"""

router = APIRouter(
    prefix="/api/herb",
    tags=["herb"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/search-herbs")
async def search_herb_by_disease(
        disease: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for searching a herb by disease

    Args:
        disease (str): the disease to search for
        token (oauth2 bearer token): the token for the user

    Returns:
        (str) The herb for the disease
    """
    if get_current_user(token) is None:
        raise credentials_exception

    return get_herb_by_disease(disease)


@router.post("/search-diseases")
async def search_herb_by_disease(
        herb: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for searching a disease by herb

    Args:
        herb (str): the herb to search for
        token (oauth2 bearer token): the token for the user

    Returns:
        (str) The disease for the herb
    """
    if get_current_user(token) is None:
        raise credentials_exception

    return get_disease_by_herb(herb)
