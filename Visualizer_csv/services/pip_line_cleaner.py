# cleaner.py
import pandas as pd
import numpy as np
import re
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from dateutil import parser


class AutoDataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def clean_column_names(self):
        self.df.columns = [col.strip().lower().replace(' ', '_') for col in self.df.columns]

    def handle_missing(self, strategy='mean'):
        imputer = SimpleImputer(strategy=strategy)
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_cols] = imputer.fit_transform(self.df[numeric_cols])

    def fix_date_columns(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                try:
                    self.df[col] = pd.to_datetime(self.df[col].map(parser.parse), errors='coerce')
                except Exception:
                    pass

    def remove_outliers(self, contamination=0.01):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            return
        iso = IsolationForest(contamination=contamination, random_state=42)
        outliers = iso.fit_predict(self.df[numeric_cols])
        self.df = self.df[outliers == 1]

    def clean_text_fields(self):
        for col in self.df.select_dtypes(include=['object', 'string']).columns:
            self.df[col] = self.df[col].astype(str).str.strip().str.lower()
            self.df[col] = self.df[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

    def execute_pipeline(self):
        self.clean_column_names()
        self.remove_duplicates()
        self.handle_missing()
        self.fix_date_columns()
        self.remove_outliers()
        self.clean_text_fields()
        return self.df
