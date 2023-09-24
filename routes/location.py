from fastapi import APIRouter

"""
    API router for location endpoint 
"""

router = APIRouter(
    prefix="/api/location",
    tags=["location"],
    responses={404: {"description": "The requested page was not found"}},
)



