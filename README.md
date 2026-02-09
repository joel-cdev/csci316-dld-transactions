## Project Overview

This project presents a large-scale data analytics pipeline built using
**Apache Spark** to analyze real-world transactional data from the
**Dubai Pulse Land Transactions dataset**.

The objective of the project is to design and implement a **scalable,
fault-tolerant, and reproducible analytics solution** that can handle
messy, transactional data and extract meaningful insights using
machine learning techniques.

The solution covers the complete big data lifecycle, including:

- Fault-tolerant data ingestion
- Schema inspection and validation
- Feature engineering at scale
- Baseline machine learning models
- Manual 10-fold cross-validation
- Custom ensemble learning from scratch
- Result analysis and interpretation
- Docker-based reproducibility

---

## Dataset Description

The dataset used in this project is the **Dubai Pulse Land Transactions**
dataset, which contains structured records of real estate transactions
conducted in Dubai over multiple years.

Key characteristics of the dataset include:

- **Transactional nature:** Each record represents a registered land or
  property transaction.
- **Mixed data types:** Numerical, categorical, temporal, and bilingual
  (Arabic/English) attributes.
- **Data quality challenges:** Missing values, malformed records, and
  inconsistent formatting.
- **Scalability considerations:** Designed to grow continuously as new
  transactions are recorded.

These characteristics justify the use of **Apache Spark** over
traditional in-memory tools such as Pandas.

---

## Why Apache Spark?

Apache Spark is used throughout this project due to:

- **Fault tolerance:** Ability to ingest and process malformed CSV data
  without pipeline failure.
- **Scalability:** Efficient handling of large, transactional datasets
  and repeated transformations.
- **Distributed processing:** Native support for parallel computation.
- **Machine learning support:** Spark ML enables scalable feature
  pipelines and model training.

All core processing is performed using **Spark DataFrames and Spark ML**.
