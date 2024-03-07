import os
from dotenv import load_dotenv
from tortoise import Tortoise

load_dotenv('../config/.env')

async def init():
    await Tortoise.init(
        db_url=os.getenv('DATABASE_URL'),
        modules={'models': ['backend.app.models.ingredient', 'backend.app.models.recipe', 'backend.app.models.user']}
    )