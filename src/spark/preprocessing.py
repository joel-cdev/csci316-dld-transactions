from pyspark.sql.functions import col


def basic_cleaning(df):
    """
    Apply minimal structural cleaning.
    """
    df = df.dropna(subset=["transaction_id", "actual_worth"])
    df = df.withColumn("actual_worth", col("actual_worth").cast("double"))
    df = df.withColumn("meter_sale_price", col("meter_sale_price").cast("double"))
    return df
