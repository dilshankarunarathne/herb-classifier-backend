from fastapi import APIRouter, Form, Depends

"""
    routers for herbs
"""

router = APIRouter(
    prefix="/api/herb",
    tags=["disease"],
    responses={404: {"description": "The requested page was not found"}},
)
