from fastapi import APIRouter
from app.schemas.water_schemas import (WaterDataSchema)
from app.db.queries import (
    insert_water_data,
    get_all_water_data,
    get_latest_water_data)

router = APIRouter(prefix="/water-data", tags=["Water Data"])

# INSERT WATER DATA
@router.post("/")
def create_water_data(
    data: WaterDataSchema):
    inserted_data = (insert_water_data(data))
    return {"message":"Water data saved successfully",
            "data": inserted_data}

# GET ALL WATER DATA
@router.get("/")
def get_water_data():
    data = (get_all_water_data())
    return {"total":len(data), "data":data}

# GET LATEST WATER DATA
@router.get("/latest")
def latest_water_data():
    latest_data = (get_latest_water_data())
    return {"data":latest_data}