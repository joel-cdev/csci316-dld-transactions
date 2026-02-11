import os

# ------------------------------
# Randomness
# ------------------------------
SEED = 42

# ------------------------------
# Data Paths
# ------------------------------
BASE_DIR = os.path.abspath(".")
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

OUTPUT_DIR = os.path.join(DATA_DIR, "outputs")

METRICS_DIR = os.path.join(OUTPUT_DIR, "metrics")
PREDICTIONS_DIR = os.path.join(OUTPUT_DIR, "predictions")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")
METADATA_DIR = os.path.join(OUTPUT_DIR, "metadata")

# ------------------------------
# ML Config
# ------------------------------
FEATURE_COL = "features"
TARGET_COL = "meter_sale_price"
