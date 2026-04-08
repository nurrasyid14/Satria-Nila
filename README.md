# **Satria-Nila**
PBL Web Service x MLOps : 

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
