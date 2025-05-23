from typing import Annotated

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Annotated[Settings, Depends(get_settings)]):
    return {"ping": "pong", "environment": settings.environment, "testing": settings.testing}
