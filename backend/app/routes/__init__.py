from fastapi import APIRouter

from .hw import router as hw_router
from .ingredients import router as ingredients_router

router = APIRouter()

router.include_router(hw_router, tags=["HelloWorld"])
router.include_router(ingredients_router, prefix="/ingredients", tags=["Ingredients"])