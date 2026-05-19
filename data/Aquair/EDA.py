import pandas as pd
import plotly.graph_objects as go
import numpy as np

import json
import os

from datetime import datetime


class EDA:

    def __init__(self):
        self.data = None

    # =====================================================
    # LOAD DATA
    # =====================================================
    def load_data(self, path):

        try:

            extension = path.split(".")[-1].lower()

            if extension == "csv":
                self.data = pd.read_csv(path)

            elif extension in ["xlsx", "xls"]:
                self.data = pd.read_excel(path)

            elif extension == "json":
                self.data = pd.read_json(path)

            elif extension == "parquet":
                self.data = pd.read_parquet(path)

            else:
                raise ValueError(
                    f"Unsupported file type: {extension}"
                )

            return self.data

        except Exception as e:
            print(f"Error loading dataset: {e}")
            return None

    # =====================================================
    # DATA INFO
    # =====================================================
    def show_info(self):

        info = {
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.astype(str).to_dict(),
            "shape": self.data.shape
        }

        return info

    # =====================================================
    # MISSING VALUES
    # =====================================================
    def show_missing_values(self):

        missing = self.data.isnull().sum().to_dict()

        return missing

    # =====================================================
    # DUPLICATES
    # =====================================================
    def check_duplicates(self):

        duplicates = int(
            self.data.duplicated().sum()
        )

        return duplicates

    # =====================================================
    # DATA TYPES
    # =====================================================
    def show_dtypes(self):

        return self.data.dtypes.astype(str).to_dict()

    # =====================================================
    # DESCRIPTIVE STATS
    # =====================================================
    def descriptive_statistics(self):

        stats = self.data.describe(
            include="all"
        ).fillna("").to_dict()

        return stats

    # =====================================================
    # SERIAL KEY GENERATOR
    # =====================================================
    def generate_serial_key(
        self,
        process_name
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )[:-3]

        return f"{process_name}-{timestamp}"

    # =====================================================
    # SAVE JSON
    # =====================================================
    def save_json(
        self,
        data,
        process_name,
        output_dir="outputs"
    ):

        os.makedirs(output_dir, exist_ok=True)

        serial_key = self.generate_serial_key(
            process_name
        )

        filename = f"{serial_key}.json"

        filepath = os.path.join(
            output_dir,
            filename
        )

        with open(filepath, "w") as f:
            json.dump(
                data,
                f,
                indent=4,
                default=str
            )

        return filepath

    # =====================================================
    # EDA PIPELINE
    # =====================================================
    def EDA_pipeline(self):

        if self.data is None:

            return {
                "status": "error",
                "message": "No dataset loaded."
            }

        # ============================================
        # RUN ALL EDA FUNCTIONS
        # ============================================

        results = {

            "dataset_overview": {
                "shape": self.data.shape,
                "total_rows": len(self.data),
                "total_columns": len(self.data.columns)
            },

            "data_info": self.show_info(),

            "missing_values":
                self.show_missing_values(),

            "duplicates":
                self.check_duplicates(),

            "data_types":
                self.show_dtypes(),

            "descriptive_statistics":
                self.descriptive_statistics()
        }

        # ============================================
        # SAVE JSON REPORT
        # ============================================

        json_path = self.save_json(
            results,
            process_name="eda-report"
        )

        # ============================================
        # RETURN WEB-FRIENDLY RESPONSE
        # ============================================

        return {

            "status": "success",

            "generated_at":
                datetime.now().isoformat(),

            "report_file":
                json_path,

            "results":
                results
        }


# from EDA import EDA
# eda = EDA()
# path = "water.csv/xls/etc..."
# eda.load_data(path)
# report = eda.EDA_pipeline()
# print(report)