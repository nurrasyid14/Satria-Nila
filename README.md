# **S A T R I A**
PBL Web Service x MLOps x Data Mining :  

"Pengembangan Eary Warning System berbasis Machine Learning untuk Klasifikasi Kualitas Air serta Mitigasi Risiko pada Biota Akuakultur"

--

"Machine Learning-Based Early Warning System Development for Water Quality Classification to Mitigate Risks among Aquacultural Biotes"
---
---
## **Deskripsi**

---
## **Overview & Alur Kerja**

---
## **Tentang Data**


| Temperature | Turbidity (cm) | Dissolved Oxygen (mg/L) | Biochemical Oxygen Demand (mg/L) | Carbon Dioxide (CO2) |     pH | Total Alkalinity (mg L-1) | Total Hardness (mg L-1) | Calcium (mg L-1) | Ammonia (mg L-1) | Nitrite (mg L-1) | Phosphorus (mg L-1) | Hydrogen Sulfide (mg L-1) | Plankton Count (No. L-1) | Water Quality Label | Aquaculture Suitability Tier | Aquaculture Suitability Description                                                                                            |
| ----------- | -------------: | ----------------------: | -------------------------------: | -------------------: | -----: | ------------------------: | ----------------------: | ---------------: | ---------------: | ---------------: | ------------------: | ------------------------: | -----------------------: | ------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 67.45       |          10.13 |                   0.208 |                            7.474 |               10.181 |  4.752 |                   218.365 |                 300.125 |          337.178 |            0.286 |            4.355 |               0.006 |                     0.067 |                   6070.0 | 2                   | Reduced Suitability          | Reduced Suitability: Water conditions are under stress and may impair aquaculture performance, fish health, or pond stability. |
| 64.63       |          94.02 |                  11.434 |                            10.86 |               14.861 |  3.085 |                    273.94 |                   8.427 |          363.661 |            0.096 |            2.183 |               0.005 |                     0.023 |                    251.0 | 2                   | Reduced Suitability          | Reduced Suitability: Water conditions are under stress and may impair aquaculture performance, fish health, or pond stability. |
| 65.12       |          90.65 |                  12.431 |                            12.81 |                12.32 |  9.649 |                   220.813 |                  11.726 |          309.371 |            0.975 |            4.902 |               0.007 |                     0.065 |                   7219.0 | 2                   | Reduced Suitability          | Reduced Suitability: Water conditions are under stress and may impair aquaculture performance, fish health, or pond stability. |
| 1.64        |           0.07 |                  10.964 |                            8.508 |               12.955 |   4.82 |                   266.572 |                   6.628 |             8.18 |            0.885 |            3.572 |               3.174 |                     0.026 |                   1230.0 | 2                   | Reduced Suitability          | Reduced Suitability: Water conditions are under stress and may impair aquaculture performance, fish health, or pond stability. |
| 64.86       |           2.12 |                   1.362 |                           13.335 |               13.603 | 10.244 |                   252.108 |                 339.892 |          253.997 |            0.802 |            4.656 |               3.855 |                     0.061 |                   1035.0 | 2                   | Reduced Suitability          | Reduced Suitability: Water conditions are under stress and may impair aquaculture performance, fish health, or pond stability. |

---
## **Algoritma & Tools** 

### **Algoritma**

### **Tools**

#### **PyCaret**

#### **MLFlow**

#### **Docker**

---
## **Folder Tree**

``` txt
smart-water-monitoring/
│
├── docker-compose.yml
├── .env
├── README.md
│
├── services/
│   │
│   ├── api-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── routes/
│   │   │   │   ├── predict.py
│   │   │   │   ├── health.py
│   │   │   │   └── water.py
│   │   │   │
│   │   │   ├── schemas/
│   │   │   │   ├── water_schema.py
│   │   │   │   └── prediction_schema.py
│   │   │   │
│   │   │   ├── services/
│   │   │   │   ├── ml_client.py
│   │   │   │   └── data_client.py
│   │   │   │
│   │   │   ├── core/
│   │   │   │   ├── config.py
│   │   │   │   └── security.py
│   │   │   │
│   │   │   └── utils/
│   │   │       └── logger.py
│   │   │
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   ├── ml-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── model/
│   │   │   │   ├── train.py
│   │   │   │   ├── predict.py
│   │   │   │   └── pipeline.py
│   │   │   │
│   │   │   ├── mlflow/
│   │   │   │   ├── tracking.py
│   │   │   │   └── registry.py
│   │   │   │
│   │   │   └── artifacts/
│   │   │       └── (saved models)
│   │   │
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   ├── data-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── db/
│   │   │   │   ├── supabase_client.py
│   │   │   │   └── queries.py
│   │   │   │
│   │   │   ├── routes/
│   │   │   │   └── water_data.py
│   │   │   │
│   │   │   └── schemas/
│   │   │       └── water_schema.py
│   │   │
│   │   ├── requirements.txt
│   │   └── Dockerfile
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── FormInput.jsx
│   │   │   ├── ResultCard.jsx
│   │   │   └── Navbar.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   └── Dashboard.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── package.json
│   └── vite.config.js
│
└── mlflow/
    ├── mlruns/
    └── Dockerfile
```

## **How to Access**

### **Windows PowerShell**
``` pwsh
x
```
### **MacOS Bash**
``` bash
x
```
### **Linux Bash**
``` bash
x
```

## **Preview Hasil (Laporan per tanggal ddmmyyyy dari file log.json)**

```json
a
```

### **Tangkapan Layar**
