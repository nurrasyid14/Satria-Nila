# SATRIA ML-Service (Inference Engine)

ML-Service adalah mesin kecerdasan buatan yang bertugas melakukan klasifikasi kualitas air berdasarkan data sensor.

## 🧠 Model Machine Learning
- **Algorithm**: Classifier (berdasarkan dataset `Refined_Aquaculture_Water_Suitability_Signals.csv`).
- **Artifacts**: Model disimpan dalam format `.pkl` di `app/domains/water/artifacts/`.
- **Target**: Memprediksi tingkat kelayakan air (Optimal, Moderate, Reduced).

## 📊 Parameter Input (14 Fitur)
Service ini menerima data sensor berupa:
- Fisik: Temperature, Turbidity, Plankton Count.
- Kimia: pH, Dissolved Oxygen, BOD, CO2, Alkalinity, Hardness, Calcium, Ammonia, Nitrite, Phosphorus, H2S.

## 💻 Cara Menjalankan
```bash
uvicorn app.main:app --reload --port 8001
```
Akses dokumentasi API di: `http://127.0.0.1:8001/docs`

## 🧪 Testing
Jalankan unit test untuk memastikan pipeline model tetap stabil:
```bash
pytest tests/
```
