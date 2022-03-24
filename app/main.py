from fastapi import FastAPI
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
from api.province_api import province_router
from api.city_api import city_router
from api.cost_api import cost_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(province_router, tags=["province"])
app.include_router(city_router, tags=["city"])
app.include_router(cost_router, tags=["cost"])

@app.get("/")
def read_root():
    return {"root": "rajaongkir-integration"}