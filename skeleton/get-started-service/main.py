from fastapi import FastAPI, HTTPException, Body
from google.cloud import firestore
# from core.config import settings
# # from db.session import engine 
# from db.base_class import Base
# from apis.base import api_router
# from db.utils import check_db_connected
# from db.utils import check_db_disconnected

# def create_tables():         
# 	Base.metadata.create_all(bind=engine)
# def include_router(app):
#     app.include_router(api_router)

# def start_application():
#     app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
#     #create_tables()
#     return app

# app = start_application()

app = FastAPI()


db = firestore.Client()

@app.get("/")
def hello():
    return {"msg":"Hello FastAPi"}


# @app.on_event("startup")
# async def app_startup():
#     await check_db_connected()


# @app.on_event("shutdown")
# async def app_shutdown():
#     await check_db_disconnected()


@app.post("/push_data")
async def push_data(data: dict = Body(...)):
    try:
        # Push data to Firestore
        doc_ref = db.collection('Datapoints').add(data)
        return {"message": "Data pushed successfully", "document_id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error pushing data to Firestore: {str(e)}")

