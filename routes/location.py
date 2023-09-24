from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.location_service import add_location, get_location

"""
    API router for location endpoint 
    
    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        get_location_for_herb: the endpoint for getting location for a herb
        add_new_location: the endpoint for adding a new location for a herb

    Raises:
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
        herb (str): the herb to search for
        token (oauth2 bearer token): the token for the user

    Returns:
        The location for the herb

    Raises:
        HTTPException: if the user is not logged in
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
    """
    The endpoint for adding a new location for a herb 
    Args:
        lon (float): the longitude of the location
        lat (float): the latitude of the location
        herb (str): the herb to add the location for
        token (oauth2 bearer token): the token for the user

    Returns:
        A message indicating the success of the operation

    Raises:
        HTTPException: if the user is not logged in
    """
    if get_current_user(token) is None:
        raise credentials_exception

    add_location(lon, lat, herb)

    return {"message": "Successfully added new location"}
