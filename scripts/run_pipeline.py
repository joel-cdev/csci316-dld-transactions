import os
import sys
import json
import datetime
import pandas as pd

sys.path.append(os.path.abspath("."))

from src.utils.config import *
from src.utils.io import ensure_directories, save_metrics
from src.spark.spark_session import create_spark_session
from src.spark.data_loader import load_data
from src.features.feature_pipeline import build_features
from src.models.baseline_models import (
    train_linear_regression,
    train_decision_tree
)
from src.models.evaluation import evaluate_model

from pyspark.sql.functions import col

def main():

    # --------------------------------------------------
    # 1️⃣ Ensure Output Directories
    # --------------------------------------------------

    ensure_directories([
        METRICS_DIR,
        PREDICTIONS_DIR,
        FIGURES_DIR,
        METADATA_DIR
    ])

    spark = create_spark_session()

    print("Loading data...")
    df = load_data(spark, os.path.join(PROCESSED_DIR, "land_transactions_cleaned.parquet"))

    print("Building features...")
    df = build_features(df)

    train_df, test_df = df.randomSplit([0.8, 0.2], seed=SEED)

    # --------------------------------------------------
    # 2️⃣ Train Models
    # --------------------------------------------------

    print("Training Linear Regression...")
    lr_model = train_linear_regression(
        train_df, FEATURE_COL, TARGET_COL
    )

    print("Training Decision Tree...")
    dt_model = train_decision_tree(
        train_df, FEATURE_COL, TARGET_COL
    )

    # --------------------------------------------------
    # 3️⃣ Evaluate
    # --------------------------------------------------

    print("Evaluating models...")

    lr_rmse, lr_r2 = evaluate_model(
        lr_model, test_df, FEATURE_COL, TARGET_COL
    )

    dt_rmse, dt_r2 = evaluate_model(
        dt_model, test_df, FEATURE_COL, TARGET_COL
    )

    results = pd.DataFrame({
        "model": ["LinearRegression", "DecisionTree"],
        "rmse": [lr_rmse, dt_rmse],
        "r2": [lr_r2, dt_r2]
    })

    save_metrics(
        results,
        os.path.join(METRICS_DIR, "baseline_metrics.csv")
    )

    # --------------------------------------------------
    # 4️⃣ Select Best Model
    # --------------------------------------------------

    if lr_rmse < dt_rmse:
        best_model = lr_model
        best_model_name = "LinearRegression"
        best_rmse = lr_rmse
    else:
        best_model = dt_model
        best_model_name = "DecisionTree"
        best_rmse = dt_rmse

    print(f"Best model: {best_model_name}")

    # --------------------------------------------------
    # 5️⃣ Save Predictions
    # --------------------------------------------------

    print("Saving predictions...")

    if "prediction" in test_df.columns:
        test_df = test_df.drop("prediction", "rawPrediction", "probability")  

    predictions = best_model.transform(test_df)

    predictions_df = predictions.select(
        col(TARGET_COL).alias("actual"),
        col("prediction").alias("predicted")
    )

    predictions_pd = predictions_df.toPandas()

    predictions_pd.to_csv(
        os.path.join(PREDICTIONS_DIR, "test_predictions.csv"),
        index=False
    )

    # --------------------------------------------------
    # 6️⃣ Save Run Metadata
    # --------------------------------------------------

    print("Saving run metadata...")

    run_info = {
        "timestamp": datetime.datetime.now().isoformat(),
        "dataset_rows": df.count(),
        "train_rows": train_df.count(),
        "test_rows": test_df.count(),
        "features_used": FEATURE_COL,
        "target": TARGET_COL,
        "best_model": best_model_name,
        "best_rmse": float(best_rmse),
        "linear_regression_rmse": float(lr_rmse),
        "decision_tree_rmse": float(dt_rmse),
        "seed": SEED
    }

    with open(os.path.join(METADATA_DIR, "run_info.json"), "w") as f:
        json.dump(run_info, f, indent=4)

    print("Pipeline complete.")
    spark.stop()

    from src.utils.generate_figures import generate_all_figures

    generate_all_figures(
        METRICS_DIR,
        PREDICTIONS_DIR,
        FIGURES_DIR
    )

if __name__ == "__main__":
    main()
