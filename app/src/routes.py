from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/test",
)
async def get_peru_products():  
    return {"message": "Hello World"}
