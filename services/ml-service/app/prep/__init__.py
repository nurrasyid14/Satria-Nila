class _Preprocessor:
    '''
    Apa saja yang dilakukan dalam Preprocessing:
    - Membersihkan Data Invalid: Membuang, atau Mengisi null; dan Mengganti nilai yang tidak valid dengan value yang sesuai.
    - Mengubah Format Data: Mengubah format data menjadi format yang sesuai untuk analisis atau pemodelan, seperti mengubah tipe data, menggabungkan kolom, atau memisahkan kolom.
    - Normalisasi atau Standarisasi: Mengubah skala data agar lebih konsisten.
    - Ekstraksi Fitur: Mengambil fitur-fitur penting dari data yang dapat digunakan untuk analisis atau pemodelan.
    - Pengkodean Kategori: Mengubah data kategori menjadi format numerik yang dapat digunakan dalam model machine learning.
    - Confidence & Importance Score: Menambahkan skor kepercayaan atau pentingnya fitur untuk membantu dalam pemilihan fitur atau interpretasi model.
    - Pruning: Menghapus fitur yang tidak relevan atau redundan untuk meningkatkan kinerja model dan mengurangi kompleksitas.
    - Rekomendasi Algoritma: Memberikan rekomendasi algoritma yang sesuai berdasarkan karakteristik data dan tujuan analisis atau pemodelan.

    Apa patokan Data dapat dikatakan Optimal untuk digunakan dalam Tahap Tahap Selanjutnya?
    - Data yang bersih dan bebas dari nilai yang tidak valid atau null.
    - Data yang memiliki format yang sesuai untuk analisis atau pemodelan.
    - Data yang telah dinormalisasi atau distandarisasi jika diperlukan.
    - Data yang memiliki fitur-fitur penting yang telah diekstraksi.
    - Data yang telah dikodekan dengan benar untuk fitur kategori.
    - Data yang memiliki skor kepercayaan atau pentingnya fitur yang telah ditambahkan.
    - Data yang telah dipruning untuk menghapus fitur yang tidak relevan atau redundan
    - Data yang telah dianalisis untuk memberikan rekomendasi algoritma yang sesuai.

    Catatan: Pipeline akan dijalankan dalam nested if-else clause, dimana:
        setiap tahapan akan dijalankan jika dan hanya jika tahapan sebelumnya telah berhasil dijalankan.
        Jika ada tahapan yang gagal, maka pipeline akan berhenti dan memberikan pesan error yang sesuai. 

    Dataset yang telah dibersihkan akan diekspor ke dalam parent/parent/parent/data/processed/<dataset_asli>_preprocessed.csv untuk digunakan dalam tahap-tahap selanjutnya.

    '''
    import pandas as pd
    import numpy as np
    import logging
    import os
    import sys

    from sklearn.preprocessing import StandardScaler
    from sklearn.feature_selection import SelectKBest, f_classif

    export_path = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'data', 'processed'
    )

    def __init__(self, dataset_path, target_col="Label", k_best=8):
        self.dataset_path = dataset_path
        self.dataset_name = os.path.basename(dataset_path).split('.')[0]

        self.target_col = target_col
        self.k_best = k_best

        self.data = None
        self.cleaned_data = None
        self.selected_features = None

    # ========================
    # LOAD
    # ========================
    def _load_data(self):
        try:
            self.data = self.pd.read_csv(self.dataset_path)
            self.logging.info(f"[LOAD] {self.dataset_name} loaded.")
            return True
        except Exception as e:
            self.logging.error(f"[LOAD ERROR] {e}")
            return False

    # ========================
    # VALIDATION (DOMAIN RULES)
    # ========================
    def _validate_ranges(self):
        try:
            df = self.data.copy()

            # Domain constraints (aquaculture-safe ranges)
            constraints = {
                "Temperature (°C)": (0, 40),
                "pH": (4, 10),
                "Dissolved Oxygen (mg/L)": (0, 20),
                "Ammonia (mg/L)": (0, 5),
            }

            for col, (low, high) in constraints.items():
                if col in df.columns:
                    df[col] = df[col].clip(lower=low, upper=high)

            self.data = df
            self.logging.info("[VALIDATION] Range constraints applied.")
            return True

        except Exception as e:
            self.logging.error(f"[VALIDATION ERROR] {e}")
            return False

    # ========================
    # CLEANING
    # ========================
    def _clean_data(self):
        try:
            df = self.data.copy()

            # Convert numeric safely
            for col in df.columns:
                df[col] = self.pd.to_numeric(df[col], errors="ignore")

            # Fill NA (median for numeric only)
            numeric_cols = df.select_dtypes(include=[self.np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

            self.cleaned_data = df
            self.logging.info("[CLEAN] Missing values handled.")
            return True

        except Exception as e:
            self.logging.error(f"[CLEAN ERROR] {e}")
            return False

    # ========================
    # NORMALIZATION
    # ========================
    def _normalize_data(self):
        try:
            df = self.cleaned_data.copy()

            scaler = self.StandardScaler()
            numeric_cols = df.select_dtypes(include=[self.np.number]).columns

            if self.target_col in numeric_cols:
                numeric_cols = numeric_cols.drop(self.target_col)

            df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

            self.cleaned_data = df
            self.logging.info("[NORMALIZE] StandardScaler applied.")
            return True

        except Exception as e:
            self.logging.error(f"[NORMALIZE ERROR] {e}")
            return False

    # ========================
    # FEATURE SELECTION
    # ========================
    def _feature_selection(self):
        try:
            df = self.cleaned_data.copy()

            X = df.drop(columns=[self.target_col])
            y = df[self.target_col]

            selector = self.SelectKBest(score_func=self.f_classif, k=self.k_best)
            X_new = selector.fit_transform(X, y)

            selected_cols = X.columns[selector.get_support()]

            self.selected_features = list(selected_cols)

            self.cleaned_data = self.pd.concat(
                [self.pd.DataFrame(X_new, columns=selected_cols), y.reset_index(drop=True)],
                axis=1
            )

            self.logging.info(f"[FEATURE] Selected: {self.selected_features}")
            return True

        except Exception as e:
            self.logging.error(f"[FEATURE ERROR] {e}")
            return False

    # ========================
    # EXPORT
    # ========================
    def export_data(self):
        try:
            os.makedirs(self.export_path, exist_ok=True)

            export_file = os.path.join(
                self.export_path,
                f"{self.dataset_name}_preprocessed.csv"
            )

            self.cleaned_data.to_csv(export_file, index=False)

            self.logging.info(f"[EXPORT] Saved to {export_file}")
            return True

        except Exception as e:
            self.logging.error(f"[EXPORT ERROR] {e}")
            return False

    # ========================
    # PIPELINE CONTROLLER
    # ========================
    def run_pipeline(self):
        if not self._load_data():
            return

        if not self._validate_ranges():
            return

        if not self._clean_data():
            return

        if not self._normalize_data():
            return

        if not self._feature_selection():
            return

        if not self.export_data():
            return

        self.logging.info("[SUCCESS] Preprocessing pipeline completed.")

__all__ = ["_Preprocessor"]