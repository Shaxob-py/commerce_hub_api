import os
from contextlib import asynccontextmanager

from admin import admin
from database.base import db
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from database.base import db
from routers import router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.create_all()
    admin.mount_to(app)
    print('project ishga tushdi')
    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', root_path='/api', title="Commerce Hub API", lifespan=lifespan, )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    msg = exc.args[0][0]['msg']
    return JSONResponse(
        {'message': msg},
        status.HTTP_400_BAD_REQUEST,
    )


app = FastAPI(
    docs_url='/',

    title="Commerce Hub API",
    description="api/vi",
    lifespan=lifespan,
)

MEDIA_DIR = os.path.join(os.getcwd(), "media")

if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)

app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://192.168.1.99:3000",
    "http://10.40.1.161:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

app.include_router(router, prefix='/api/v1')
