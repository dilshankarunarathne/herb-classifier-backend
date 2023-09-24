from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.location_service import add_location

"""
    API router for location endpoint 
"""

router = APIRouter(
    prefix="/api/location",
    tags=["location"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post()
async def get_location_for_herb(
    herb: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception


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
