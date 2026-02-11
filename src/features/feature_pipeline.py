from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import RandomForestRegressor


def build_features(df):

    from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import RandomForestRegressor


def build_features(df):

    # Drop old model outputs if present
    for col in ["prediction", "rawPrediction", "probability"]:
        if col in df.columns:
            df = df.drop(col)

    assembler = VectorAssembler(
        inputCols=[
            "meter_sale_price",
            "procedure_area",
            "rent_value"
        ],
        outputCol="features",
        handleInvalid="skip"
    )

    rf = RandomForestRegressor(
        featuresCol="features",
        labelCol="actual_worth"
    )

    pipeline = Pipeline(stages=[assembler, rf])

    pipeline_model = pipeline.fit(df)

    return pipeline_model.transform(df)
