# services/data-service/app/db/supabase_client.py

import os
# pyrefly: ignore [missing-import]
from supabase import create_client, Client
from dotenv import load_dotenv

# Path ke file .env yang ada di root direktori proyek (naik 4 tingkat dari app/db/)
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '.env')
load_dotenv(dotenv_path=env_path)

# Ambil URL dan Key dari environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # Bisa diganti SUPABASE_SERVICE_ROLE_KEY jika butuh akses admin

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Variabel environment SUPABASE_URL atau SUPABASE_KEY belum ditemukan. Pastikan file .env sudah diisi.")

# Inisialisasi client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Supabase client berhasil diinisialisasi!")
