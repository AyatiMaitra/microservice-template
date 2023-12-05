from fastapi import FastAPI
from core.config import settings
from db.session import engine 
#from db.base_class import Base
from apis.base import api_router
from db.utils import check_db_connected
from db.utils import check_db_disconnected

# def create_tables():         
# 	Base.metadata.create_all(bind=engine)
def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    #create_tables()
    return app

app = start_application()

# @app.get("/")
# def hello():
#     return {"msg":"Hello FastAPi"}


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()