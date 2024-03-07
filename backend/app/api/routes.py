from fastapi import APIRouter
from .routes.hw import router as hw_router

router = APIRouter()

router.include_router(hw_router, prefix="/", tags=["HelloWorld"])