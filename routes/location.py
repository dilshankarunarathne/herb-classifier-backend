from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.location_service import add_location, get_location

"""
    API router for location endpoint 
    get_location_for_herb: get location for a herb (POST)  /api/location/get-location  (form-data) herb
    add_new_location: add a new location (POST)  /api/location/add-location  (form-data) lon, lat, herb 
"""

router = APIRouter(
    prefix="/api/location",
    tags=["location"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/get-location")
async def get_location_for_herb(
    herb: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for getting location for a herb
    Args:
        herb: the herb to search for
        token: the token for the user
        
    Returns:
    The location for the herb

    :raises HTTPException: if the user is not logged in
    """
    if get_current_user(token) is None:
        raise credentials_exception

    return get_location(herb)


@router.post("/add-location")
async def add_new_location(
    lon: float = Form(...),
    lat: float = Form(...),
    herb: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    add_location(lon, lat, herb)

    return {"message": "Successfully added new location"}
