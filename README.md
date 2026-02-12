# CSCI316 — Large-Scale Real Estate Analytics (Dubai Land Transactions)

**Course:** Big Data Mining and Applications
**Institution:** University of Wollongong in Dubai
**Framework:** Apache Spark + Custom ML + Docker + Streamlit

---

## Overview

This project implements a **Spark-native large-scale machine learning pipeline** for modeling Dubai real estate transaction prices using public land transaction data.

The system demonstrates:

* Distributed data processing with Apache Spark
* Explicit schema enforcement and cleaning
* Manual 10-fold cross validation (no library shortcuts)
* Custom ensemble learning implementation
* Reproducible containerized environment (Docker)
* Interactive results dashboard (Streamlit)

The focus of this project is **system design, scalability, and reproducibility**, not just predictive accuracy.

---

## Problem Statement

Can we model real estate price-per-meter variation in Dubai using structured transaction data while ensuring scalability and robustness?

Challenges include:

* Large dataset size
* Missing values and inconsistent schemas
* Heavy-tailed price distributions
* Mixed numeric and categorical data
* Real-world noise and outliers

This project builds a distributed ML pipeline to address these challenges.

---

## Dataset

**Source:** Dubai Pulse — Land Transactions Dataset

Characteristics:

* Multi-year transaction records
* Numeric + categorical + temporal attributes
* Bilingual fields (Arabic + English)
* Missing values and inconsistent formatting
* Transaction-level granularity

These characteristics justify distributed processing using Spark instead of Pandas.

---

## Why Apache Spark?

Spark was selected because:

| Challenge                | Spark Justification            |
| ------------------------ | ------------------------------ |
| Large dataset            | Distributed processing         |
| Memory constraints       | Lazy execution model           |
| Fault tolerance          | Resilient distributed datasets |
| Repeated transformations | Optimized execution planning   |

Processing this dataset purely with Pandas would be inefficient and non-scalable.

---

## System Architecture

```
Raw Dataset
    ↓
Spark Ingestion
    ↓
Schema Enforcement & Cleaning
    ↓
Feature Engineering
    ↓
Baseline Models
    ↓
Manual 10-Fold Cross Validation
    ↓
Custom Ensemble
    ↓
Metrics + Predictions + Figures
    ↓
Streamlit Dashboard
```

---

## Pipeline Components

### Data Layer

* Explicit schema definition
* Null handling
* Type casting
* Data validation
* Partition-aware transformations

### Feature Engineering

* VectorAssembler
* StandardScaler
* Numeric feature selection
* Target exclusion enforcement

### Baseline Models

* Linear Regression
* Decision Tree Regressor

### Manual Cross Validation

* Manual 10-fold splitting
* Train on 9 folds
* Validate on 1 fold
* Metric aggregation

No use of:

* `CrossValidator`
* `GridSearchCV`
* Built-in Spark CV utilities

### Custom Ensemble

* Bagging implementation
* Bootstrap sampling
* Majority/mean aggregation
* No use of RandomForest or GradientBoosting APIs

---

## Results Summary

| Model             | RMSE     | R²      |
| ----------------- | -------- | ------- |
| Linear Regression | ~344,000 | ~0.001  |
| Decision Tree     | ~345,000 | ~0.0004 |

### Interpretation

* Extremely low R² indicates strong underfitting.
* Linear regression cannot capture nonlinear structure.
* Decision tree slightly stabilizes variance but still weak.
* Ensemble improves robustness but not dramatically.

The primary bottleneck is **feature richness**, not model type.

---

## Key Insights

* Price distribution is heavy-tailed.
* Errors increase for high-value properties (heteroscedasticity).
* Residuals are not normally distributed.
* Dataset contains significant noise.
* Feature engineering is critical for performance.

---

## Limitations

* Limited feature set
* No categorical encoding yet
* No spatial proximity features
* No time-trend modeling
* No hyperparameter tuning

These were deliberate constraints to prioritize system architecture validation.

---

## Future Work

* Log-transform target variable
* Add categorical encoding (location, property type)
* Incorporate temporal trend features
* Spatial feature engineering
* Gradient boosting models
* Production API deployment
* Distributed hyperparameter tuning

---

## Repository Structure

```
data/
  raw/
  processed/
  outputs/
     metrics/
     predictions/
     figures/
     metadata/

notebooks/
scripts/
src/
   spark/
   features/
   models/
   ensemble/
   validation/
   utils/

streamlit_app.py
Dockerfile
requirements.txt
README.md
```

---

## Generated Artifacts

Running the pipeline produces:

* `baseline_metrics.csv`
* `cv_results.csv`
* `ensemble_metrics.csv`
* `test_predictions.csv`
* `run_info.json`
* Evaluation plots (RMSE comparison, residual distribution, etc.)

These artifacts power the Streamlit dashboard.

---

## How to Run

### Install dependencies

```
pip install -r requirements.txt
```

### Run the full Spark pipeline

```
python scripts/run_pipeline.py
```

### Launch Streamlit dashboard

```
streamlit run streamlit_app.py
```

---

## Docker (UI Only)

Docker is used to containerize the Streamlit showcase for reproducibility.

Build image:

```
docker build -t dld-streamlit .
```

Run container:

```
docker run -p 8501:8501 dld-streamlit
```

---

## References

* Apache Spark Documentation
* Dubai Pulse Data Portal
* Hastie, Tibshirani & Friedman — *Elements of Statistical Learning*
* Géron — *Hands-On Machine Learning*

---

## Final Takeaway

This project demonstrates:

* Scalable distributed ML pipeline design
* Manual validation logic implementation
* Custom ensemble development
* Reproducible containerized deployment

Accuracy can be improved.

System design must come first.
