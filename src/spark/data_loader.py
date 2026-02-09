def load_clean_data(spark, path):
    """
    Load cleaned Parquet dataset.
    """
    return spark.read.parquet(path)