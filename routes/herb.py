from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme

"""
    routers for herbs
"""

router = APIRouter(
    prefix="/api/herb",
    tags=["herb"],
    responses={404: {"description": "The requested page was not found"}},
)

@router.post()
async def search_herb_by_disease(
    disease: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
