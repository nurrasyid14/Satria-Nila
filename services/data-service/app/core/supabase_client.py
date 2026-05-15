# services/data-service/app/core/supabase_client.py
from supabase import create_client, Client
from .config import get_settings

def get_supabase() -> Client:
    """
    Mengembalikan instance Supabase client yang segar berdasarkan settings saat ini.
    """
    settings = get_settings()
    # Inisialisasi client on-demand untuk menghindari stale state saat reload
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
