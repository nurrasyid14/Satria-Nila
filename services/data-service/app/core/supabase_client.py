# services/data-service/app/core/supabase.py
# INFRASTRUCTURE: Inisialisasi Supabase Client (Singleton Pattern)
# Menggantikan db/supabase_client.py yang menggunakan os.getenv() langsung

from supabase import create_client, Client
from .config import get_settings

# Inisialisasi client sekali saat modul di-import
_settings = get_settings()
supabase: Client = create_client(_settings.SUPABASE_URL, _settings.SUPABASE_KEY)


def get_supabase() -> Client:
    """
    Mengembalikan instance Supabase client.
    Digunakan oleh routes untuk melakukan operasi database.
    """
    return supabase
