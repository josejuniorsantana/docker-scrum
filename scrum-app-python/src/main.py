from imp import reload
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router


from infrastructure import models, schemas
from infrastructure.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(root_path="/api_v2")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")



if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, log_level="info", reload=True)
    print("running")