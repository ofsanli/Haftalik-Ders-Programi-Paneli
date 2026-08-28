from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.database import init_db
from app.routes import router
from app.ui import home, panel


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Haftalık Ders Programı Paneli", lifespan=lifespan)

app.add_api_route("/", home, methods=["GET"], response_class=HTMLResponse)
app.add_api_route("/panel", panel, methods=["GET"], response_class=HTMLResponse)
app.include_router(router)

