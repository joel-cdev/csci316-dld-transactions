from pyspark.sql.types import (
    StructType, StructField,
    StringType, DoubleType, IntegerType, DateType
)


def get_expected_schema():
    """
    Returns an expected schema for documentation and validation purposes.
    This schema is not strictly enforced during ingestion.
    """
    return StructType([
        StructField("transaction_id", StringType(), True),
        StructField("actual_worth", DoubleType(), True),
        StructField("meter_sale_price", DoubleType(), True),
        StructField("procedure_area", DoubleType(), True),
        StructField("has_parking", IntegerType(), True),
    ])
