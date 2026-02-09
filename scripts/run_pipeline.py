"""
CSCI316 – Large-Scale Analytics Pipeline Runner

This script runs the full data processing and modeling pipeline
end-to-end using Apache Spark. It is designed to be executed inside
a Docker container or any Spark-compatible environment.

Pipeline stages:
1. Load cleaned Parquet data
2. Feature engineering
3. Baseline modeling
4. Manual cross-validation
5. Custom ensemble learning
"""

from pyspark.sql import SparkSession

# Import pipeline components
from src.spark.data_loader import load_clean_data
from src.features.feature_pipeline import build_feature_dataset
from src.models.baseline_models import run_baseline_models
from src.validation.manual_cv import run_manual_cv
from src.ensemble.bagging import run_bagging_ensemble


def main():
    # --------------------------------------------------
    # 1. Initialize Spark
    # --------------------------------------------------
    spark = SparkSession.builder \
        .appName("CSCI316_Large_Scale_Analytics") \
        .getOrCreate()

    print("Spark session started.")

    # --------------------------------------------------
    # 2. Load Cleaned Data
    # --------------------------------------------------
    print("Loading cleaned dataset...")
    df_clean = load_clean_data(
        spark,
        path="data/processed/land_transactions_cleaned.parquet"
    )

    # --------------------------------------------------
    # 3. Feature Engineering
    # --------------------------------------------------
    print("Running feature engineering...")
    df_features = build_feature_dataset(df_clean)

    # --------------------------------------------------
    # 4. Baseline Models
    # --------------------------------------------------
    print("Running baseline models...")
    run_baseline_models(df_features)

    # --------------------------------------------------
    # 5. Manual 10-Fold Cross-Validation
    # --------------------------------------------------
    print("Running manual 10-fold cross-validation...")
    run_manual_cv(df_features)

    # --------------------------------------------------
    # 6. Custom Ensemble Learning
    # --------------------------------------------------
    print("Running custom bagging ensemble...")
    run_bagging_ensemble(df_features)

    print("Pipeline execution completed successfully.")

    spark.stop()


if __name__ == "__main__":
    main()