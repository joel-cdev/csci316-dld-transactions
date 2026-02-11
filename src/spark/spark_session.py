import os
from pyspark.sql import SparkSession

def create_spark_session():
    os.environ["JAVA_HOME"] = "/opt/homebrew/Cellar/openjdk@11/11.0.30/libexec/openjdk.jdk/Contents/Home"

    return (
        SparkSession.builder
        .appName("csci316")
        .master("local[*]")
        .getOrCreate()
    )
