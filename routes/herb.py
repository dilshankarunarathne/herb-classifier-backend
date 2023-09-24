from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.herb_service import get_herb_by_disease, get_disease_by_herb

"""
    routers for herbs
    search_herb_by_disease: search for a herb by disease (POST)  /api/herb/search-herbs  (form-data) disease
    search_disease_by_herb: search for a disease by herb (POST)  /api/herb/search-diseases  (form-data) herb
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
    :param disease: the disease to search for
    :param token: the token of the user
    :return: the herb details
    if get_current_user(token) is None:
        raise credentials_exception

    return get_herb_by_disease(disease)


@router.post("/search-diseases")
async def search_herb_by_disease(
        herb: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    return get_disease_by_herb(herb)
