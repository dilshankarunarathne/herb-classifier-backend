import cv2
import numpy as np
from fastapi import APIRouter, Form, Depends, UploadFile, File

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from classifier.main import recognize_plant
from services.herb_service import get_herb_by_disease, get_disease_by_herb

"""
    API router for herb endpoint

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        [POST] /api/herb/search-herbs
        search_herb_by_disease: the endpoint for searching a herb by disease

        [POST] /api/herb/search-diseases
        search_herb_by_disease: the endpoint for searching a disease by herb

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
    if await get_current_user(token) is None:
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
    if await get_current_user(token) is None:
        raise credentials_exception

    return get_disease_by_herb(herb)


@router.post("/evaluate")
async def evaluate_image(
        image: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
):
    """
    
    :param image:
    :param token:
    :return:
    """
    if image.content_type != "image/jpeg":
        return "Only jpeg images are supported"

    if get_current_user(token) is None:
        raise credentials_exception

    contents = await image.read()
    nparray = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    return recognize_plant(img)
