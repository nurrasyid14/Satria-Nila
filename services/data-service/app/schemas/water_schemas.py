from pydantic import BaseModel
from typing import Optional


class WaterDataSchema(BaseModel):
    temperature: float
    turbidity_cm: float
    dissolved_oxygen: float
    biochemical_oxygen_demand: Optional[float] = None
    carbon_dioxide: Optional[float] = None
    ph: float
    total_alkalinity: Optional[float] = None
    total_hardness: Optional[float] = None
    calcium: Optional[float] = None
    ammonia: float
    nitrite: Optional[float] = None
    phosphorus: Optional[float] = None
    hydrogen_sulfide: Optional[float] = None
    plankton_count: Optional[float] = None