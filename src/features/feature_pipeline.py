from pyspark.ml.feature import VectorAssembler, StandardScaler


def build_features(df):

    # Drop any previous prediction columns
    for c in ["prediction", "rawPrediction", "probability"]:
        if c in df.columns:
            df = df.drop(c)

    # Explicitly exclude the target column
    feature_columns = [
        "procedure_area",
        "rent_value"
    ]

    assembler = VectorAssembler(
        inputCols=feature_columns,
        outputCol="features",
        handleInvalid="skip"
    )

    df = assembler.transform(df)

    # Optional scaling (recommended for LR)
    scaler = StandardScaler(
        inputCol="features",
        outputCol="scaled_features",
        withMean=True,
        withStd=True
    )

    scaler_model = scaler.fit(df)
    df = scaler_model.transform(df)

    return df
