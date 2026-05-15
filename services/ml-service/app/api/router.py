# services/ml-service/app/api/router.py
# APPLICATION LAYER: Endpoint REST API untuk inferensi ML

from fastapi import APIRouter, HTTPException
from ..domains.water.schema import WaterQualityInput
from ..domains.water.predict import get_prediction

router = APIRouter(tags=["Inference"])


@router.post("/predict/water")
def predict_water_quality(data: WaterQualityInput):
    """
    Endpoint inferensi kualitas air.
    Menerima 14 parameter fisikokimia, mengembalikan label prediksi + confidence.
    """
    try:
        # Mapping dari field API ke kolom CSV model dilakukan di Domain (schema)
        input_dict = data.to_csv_columns()

        # Panggil fungsi inferensi dari Domain Layer
        result = get_prediction(input_dict)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
