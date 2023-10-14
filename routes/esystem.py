from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.disease_service import get_disease_details, add_disease

"""
    API router for esystem (expert system) endpoint

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        

    Raises:
        HTTPException: if the user is not logged in
"""

router = APIRouter(
    prefix="/api/esystem",
    tags=["disease"],
    responses={404: {"description": "The requested page was not found"}},
)