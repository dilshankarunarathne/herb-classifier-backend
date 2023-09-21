from fastapi import APIRouter, Form, Depends

"""
    routers for herbs
"""

router = APIRouter(
    prefix="/api/herb",
    tags=["herb"],
    responses={404: {"description": "The requested page was not found"}},
)

@router.post()
