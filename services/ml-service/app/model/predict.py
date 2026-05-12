# Services /ml-service/app/model/predict.py

from pycaret.classification import load_model, predict_model
import pandas as pd
import os

# Menentukan path absolut ke model di folder artifacts
# Base dir: services/ml-service/app/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'artifacts', 'best_pycaret_model')

try:
    # Memuat model sekali ke dalam memori agar proses prediksi lebih cepat
    model = load_model(MODEL_PATH)
    print("Model berhasil dimuat dari:", MODEL_PATH)
except Exception as e:
    print(f"Error memuat model: {e}")
    model = None

def get_prediction(input_data: dict) -> dict:
    """
    Fungsi untuk melakukan inferensi menggunakan model PyCaret.
    """
    if model is None:
        raise Exception("Model ML belum dimuat atau tidak ditemukan.")

    # PyCaret membutuhkan input berupa Pandas DataFrame
    data_df = pd.DataFrame([input_data])
    
    # Melakukan prediksi
    predictions = predict_model(model, data=data_df)
    
    # Mengekstrak hasil (Biasanya PyCaret output 'prediction_label' dan 'prediction_score')
    label = str(predictions['prediction_label'].iloc[0])
    
    score = 0.0
    if 'prediction_score' in predictions.columns:
        score = float(predictions['prediction_score'].iloc[0])
        
    return {
        "prediction": label,
        "confidence": score
    }
