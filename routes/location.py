from fastapi import APIRouter, Form

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
    herb: str = 
):
