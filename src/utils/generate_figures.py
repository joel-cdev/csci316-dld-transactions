import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def generate_all_figures(metrics_dir, predictions_dir, figures_dir):

    os.makedirs(figures_dir, exist_ok=True)

    # ==================================================
    # 1️⃣ Baseline Model Comparison
    # ==================================================

    baseline_path = os.path.join(metrics_dir, "baseline_metrics.csv")

    baseline_df = None

    if os.path.exists(baseline_path):
        baseline_df = pd.read_csv(baseline_path)

        plt.figure()
        plt.bar(baseline_df["model"], baseline_df["rmse"])
        plt.title("Baseline Model RMSE Comparison")
        plt.xticks(rotation=45)
        plt.ylabel("RMSE")
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "rmse_comparison.png"))
        plt.close()

    # ==================================================
    # 2️⃣ Cross-Validation Stability
    # ==================================================

    cv_path = os.path.join(metrics_dir, "cv_results.csv")

    if os.path.exists(cv_path):
        cv_df = pd.read_csv(cv_path)

        plt.figure()

        if "lr_rmse" in cv_df.columns:
            plt.plot(
                cv_df["fold"],
                cv_df["lr_rmse"],
                marker="o",
                label="Linear Regression"
            )

        if "dt_rmse" in cv_df.columns:
            plt.plot(
                cv_df["fold"],
                cv_df["dt_rmse"],
                marker="o",
                label="Decision Tree"
            )

        plt.title("10-Fold Cross Validation RMSE")
        plt.xlabel("Fold")
        plt.ylabel("RMSE")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "cv_stability.png"))
        plt.close()

        # Distribution Plot
        plt.figure()

        if "lr_rmse" in cv_df.columns:
            sns.histplot(cv_df["lr_rmse"], alpha=0.5, label="LR", kde=True)

        if "dt_rmse" in cv_df.columns:
            sns.histplot(cv_df["dt_rmse"], alpha=0.5, label="DT", kde=True)

        plt.title("RMSE Distribution Across Folds")
        plt.xlabel("RMSE")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "cv_distribution.png"))
        plt.close()

    # ==================================================
    # 3️⃣ Ensemble Comparison
    # ==================================================

    ensemble_path = os.path.join(metrics_dir, "ensemble_metrics.csv")

    if os.path.exists(ensemble_path) and baseline_df is not None:

        ensemble_df = pd.read_csv(ensemble_path)

        combined = pd.concat([
            baseline_df[["model", "rmse"]],
            ensemble_df[["model", "rmse"]]
        ])

        combined = combined.sort_values("rmse")

        plt.figure()
        plt.bar(combined["model"], combined["rmse"])
        plt.title("Baseline vs Ensemble RMSE")
        plt.xticks(rotation=45)
        plt.ylabel("RMSE")
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "ensemble_comparison.png"))
        plt.close()

    # ==================================================
    # 4️⃣ Residual & Prediction Analysis
    # ==================================================

    predictions_path = os.path.join(predictions_dir, "test_predictions.csv")

    if os.path.exists(predictions_path):

        pred_df = pd.read_csv(predictions_path)

        pred_df["residual"] = pred_df["actual"] - pred_df["predicted"]

        # Residual Distribution
        plt.figure()
        sns.histplot(pred_df["residual"], bins=50, kde=True)
        plt.title("Residual Distribution")
        plt.xlabel("Residual")
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "residual_distribution.png"))
        plt.close()

        # Predicted vs Actual
        plt.figure()
        plt.scatter(pred_df["actual"], pred_df["predicted"], alpha=0.3)

        max_val = max(
            pred_df["actual"].max(),
            pred_df["predicted"].max()
        )

        plt.plot([0, max_val], [0, max_val])
        plt.xlabel("Actual Price")
        plt.ylabel("Predicted Price")
        plt.title("Predicted vs Actual")
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "pred_vs_actual.png"))
        plt.close()

        # RMSE by Price Segment
        pred_df["price_bucket"] = pd.qcut(
            pred_df["actual"],
            q=5,
            duplicates="drop"
        )

        bucket_rmse = pred_df.groupby("price_bucket").apply(
            lambda x: np.sqrt(
                np.mean((x["actual"] - x["predicted"]) ** 2)
            )
        )

        plt.figure()
        bucket_rmse.plot(kind="bar")
        plt.title("RMSE by Price Segment")
        plt.ylabel("RMSE")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(figures_dir, "rmse_by_segment.png"))
        plt.close()

    print("Figures generated successfully.")
