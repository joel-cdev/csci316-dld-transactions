import os
import pandas as pd


def ensure_directories(dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)


def save_metrics(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
