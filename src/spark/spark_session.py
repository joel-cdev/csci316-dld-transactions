from pyspark.sql import SparkSession


def get_spark_session(app_name="CSCI316_Spark_App"):
    """
    Create and return a SparkSession.
    """
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
