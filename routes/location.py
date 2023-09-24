from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user

"""
    API router for location endpoint 
"""

router = APIRouter(
    prefix="/api/location",
    tags=["location"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post()
async def add_new_location(
    lon: float = Form(...),
    lat: float = Form(...),
    herb: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception
