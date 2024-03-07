from tortoise import Tortoise

from init_db import init

async def run():
    await init()
    await Tortoise.generate_schemas()

Tortoise.run_async(run())