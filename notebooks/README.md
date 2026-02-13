# Notebooks Directory – Usage and Execution Environment

## Overview

This directory contains the Jupyter notebooks used to develop, validate, and document the large-scale analytics pipeline for the **CSCI316: Big Data Mining and Applications – Project 1**.

Each notebook corresponds to a **specific stage of the big data lifecycle**, progressing sequentially from raw data ingestion to feature engineering, machine learning, evaluation, and result analysis. The notebooks are intentionally modular to improve clarity, traceability, and alignment with the project’s grading criteria.

---

## Execution Environment (Google Colab)

During development, the notebooks in this directory were executed primarily using **Google Colab** as a cloud-based notebook environment.

Google Colab was used **only as an execution host**, not as a data processing framework. All data ingestion, preprocessing, feature engineering, and machine learning logic is implemented using **Apache Spark**, ensuring that the analytical workflow remains fully Spark-native and independent of the notebook platform.

Colab was selected during development for the following reasons:
- Consistent execution environment across a 10-member team
- Reduced local hardware constraints when handling large and messy datasets
- Faster iteration and debugging of Spark-based pipelines
- Simplified collaboration and sharing during early experimentation

---

## Spark Usage Guarantee

Regardless of the execution environment:

- All ingestion and preprocessing are performed using **Spark DataFrames**
- All machine learning models are implemented using **Spark ML**
- Pandas is not used for core data processing or modeling
- Manual 10-fold cross-validation is implemented explicitly (no library CV utilities)
- Ensemble learning logic is implemented from scratch

As a result, the notebooks represent a **true large-scale analytics workflow**, even when executed in a hosted notebook environment.

---

## Reproducibility and Environment Independence

The analytical pipeline is **not dependent on Google Colab**.

To ensure reproducibility and deployment readiness:
- All reusable logic is implemented in the `src/` directory
- Notebooks act as orchestration, experimentation, and documentation layers
- The final solution is containerized using Docker and can be executed end-to-end in any Spark-compatible environment without relying on Colab

---

## Notebook Structure and Purpose

The notebooks should be read and executed in the following order:

| Notebook | Purpose |
|--------|---------|
| `00_raw_ingestion_and_cleaning.ipynb` | One-time ingestion and structural cleaning of the raw dataset |
| `01_data_validation.ipynb` | Validation and sanity checks on the cleaned Parquet dataset |
| `02_feature_engineering.ipynb` | Feature encoding, scaling, and vector assembly using Spark |
| `03_baseline_models.ipynb` | Training and evaluation of baseline machine learning models |
| `04_manual_10fold_cv.ipynb` | Manual implementation of 10-fold cross-validation |
| `05_custom_ensemble.ipynb` | Custom bagging or boosting ensemble implemented from scratch |
| `05_custom_ensemble_combined_ml_cv.ipynb` | Combined baseline training, manual CV, and bagging ensemble evaluation |


