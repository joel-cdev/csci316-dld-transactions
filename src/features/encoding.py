from pyspark.ml.feature import StringIndexer, OneHotEncoder


def build_categorical_encoders(categorical_cols):
    """
    Create StringIndexers and OneHotEncoders for categorical columns.
    """
    indexers = [
        StringIndexer(
            inputCol=col,
            outputCol=f"{col}_idx",
            handleInvalid="keep"
        )
        for col in categorical_cols
    ]

    encoders = [
        OneHotEncoder(
            inputCol=f"{col}_idx",
            outputCol=f"{col}_ohe"
        )
        for col in categorical_cols
    ]

    return indexers, encoders
