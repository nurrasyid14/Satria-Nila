from fastapi import FastAPI
from app.routes.water_data import (router as water_router)

app = FastAPI(title="Water Data Service", 
            version="1.0.0")

@app.get("/")
def root():
    return {"message": "Water Data Service Running"}

app.include_router(water_router)