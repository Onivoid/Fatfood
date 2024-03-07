from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_helloWorld():
    return {"message": "Hello World!"}