from pyspark.sql.functions import col

def load_data(spark, path):
    df = spark.read.parquet(path)

    df = (
        df
        .withColumn("procedure_area", col("procedure_area").cast("double"))
        .withColumn("rent_value", col("rent_value").cast("double"))
        .withColumn("meter_sale_price", col("meter_sale_price").cast("double"))
        .withColumn("actual_worth", col("actual_worth").cast("double"))
    )

    return df
