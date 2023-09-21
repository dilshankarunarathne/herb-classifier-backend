from fastapi import APIRouter

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
    disease: str,
    token: str = Depends(oauth2_scheme)
):
    # TODO implement this
    pass
