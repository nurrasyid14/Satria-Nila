# services/data-service/app/core/config.py
# INFRASTRUCTURE: Sentralisasi konfigurasi environment variables
# Menggunakan os.getenv dengan validasi eksplisit

import os
from functools import lru_cache
from dotenv import load_dotenv


def _find_and_load_env():
    """Mencari file .env di lokasi yang mungkin dan memuatnya."""
    base = os.path.dirname(__file__)
    candidates = [
        os.path.join(base, '..', '..', '..', '.env'),       # services/.env
        os.path.join(base, '..', '..', '..', '..', '.env'),  # root .env
    ]
    for path in candidates:
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path):
            load_dotenv(dotenv_path=abs_path)
            return abs_path
    return None


class Settings:
    """
    Konfigurasi yang dibaca dari file .env.
    Atribut divalidasi saat inisialisasi — error jika tidak ditemukan.
    """

    def __init__(self):
        _find_and_load_env()
        self.SUPABASE_URL = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY = os.getenv("SUPABASE_KEY")

        if not self.SUPABASE_URL or not self.SUPABASE_KEY:
            raise ValueError(
                "SUPABASE_URL dan SUPABASE_KEY wajib diisi. "
                "Pastikan file .env sudah ada di services/ atau root project."
            )


@lru_cache()
def get_settings() -> Settings:
    """
    Singleton: Settings hanya dibaca dari disk sekali,
    kemudian di-cache di memori untuk semua request berikutnya.
    """
    return Settings()
