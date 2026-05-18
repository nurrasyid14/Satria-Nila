# dev.ps1 - Menjalankan semua service backend Satria-Nila tanpa Docker
# Cara pakai: .\dev.ps1

Write-Host "Memulai semua backend services..." -ForegroundColor Cyan

# Pastikan venv aktif jika ada
if (Test-Path "venv\Scripts\Activate.ps1") {
    . venv\Scripts\Activate.ps1
}

# Jalankan ML Service di background
Write-Host "Starting ML Service on port 8001..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd services/ml-service; if (Test-Path '..\..\venv\Scripts\Activate.ps1') { . ..\..\venv\Scripts\Activate.ps1 }; uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload"

# Jalankan Data Service di background
Write-Host "Starting Data Service on port 8002..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd services/data-service; if (Test-Path '..\..\venv\Scripts\Activate.ps1') { . ..\..\venv\Scripts\Activate.ps1 }; uvicorn app.main:app --host 127.0.0.1 --port 8002 --reload"

# Jalankan API Service (Foreground)
Write-Host "Starting API Gateway on port 8000..." -ForegroundColor Green
cd services/api-service
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
