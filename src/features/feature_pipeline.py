from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler

from .encoding import build_categorical_encoders
from .scaling import build_scaler


def build_feature_dataset(df,
                          numeric_cols=None,
                          categorical_cols=None):
    """
    Build and apply a Spark ML feature engineering pipeline.
    """
    if numeric_cols is None or categorical_cols is None:
        return df  # notebooks handle full logic

    indexers, encoders = build_categorical_encoders(categorical_cols)

    assembler = VectorAssembler(
        inputCols=numeric_cols + [f"{c}_ohe" for c in categorical_cols],
        outputCol="features"
    )

    scaler = build_scaler()

    pipeline = Pipeline(
        stages=indexers + encoders + [assembler, scaler]
    )

    model = pipeline.fit(df)
    return model.transform(df)
