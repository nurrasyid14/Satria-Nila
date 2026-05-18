from app.db.supabase_client import supabase

# INSERT WATER SENSOR DATA
def insert_water_data(data):
    response = (supabase.table("water_sensor_data").insert({"temperature": data.temperature,
            "turbidity_cm": data.turbidity_cm,
            "dissolved_oxygen": data.dissolved_oxygen,
            "biochemical_oxygen_demand": data.biochemical_oxygen_demand,
            "carbon_dioxide": data.carbon_dioxide,
            "ph": data.ph,
            "total_alkalinity": data.total_alkalinity,
            "total_hardness": data.total_hardness,
            "calcium": data.calcium,
            "ammonia": data.ammonia,
            "nitrite": data.nitrite,
            "phosphorus": data.phosphorus,
            "hydrogen_sulfide": data.hydrogen_sulfide,
            "plankton_count": data.plankton_count}).execute())

    return response.data


# GET ALL WATER DATA
def get_all_water_data():
    response = (supabase.table("water_sensor_data").select("*").order("created_at", desc=True).execute())
    return response.data


# GET LATEST DATA
def get_latest_water_data():
    response = (supabase.table("water_sensor_data").select("*")
        .order("created_at", desc=True)
        .limit(1)
        .execute())
    return response.data


# INSERT PREDICTION LOG
def insert_prediction_log(water_sample_id, water_quality_label,
                        suitability_tier,confidence_score):

    response = (supabase.table("prediction_logs").insert({"water_sample_id": water_sample_id,
            "water_quality_label": water_quality_label,
            "aquaculture_suitability_tier": suitability_tier,
            "confidence_score": confidence_score}).execute())

    return response.data