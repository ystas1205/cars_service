import uvicorn


from fastapi_users import FastAPIUsers

from cars_api.router import router as router_cars
from src.user.auth import auth_backend
from src.user.manager import get_user_manager
from src.user.models import User
from src.user.shema import UserCreate, UserRead

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
###############################################################################
""" Настройка кэширования"""
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(title="APIcars", lifespan=lifespan)



@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")
###############################################################################
""" Роутер для cars"""
app.include_router(router_cars)
###############################################################################

""" Настройки роутеров дял user """
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
