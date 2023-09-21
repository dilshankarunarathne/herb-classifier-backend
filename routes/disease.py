from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme

"""
    routers for authentication
"""

router = APIRouter(
    prefix="/api/disease",
    tags=["disease"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("search")
async def search_disease(
    disease: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    # TODO implement this
    pass
