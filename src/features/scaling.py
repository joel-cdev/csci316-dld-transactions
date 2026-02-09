from pyspark.ml.feature import StandardScaler


def build_scaler(input_col="features", output_col="scaled_features"):
    """
    Build a StandardScaler for feature normalization.
    """
    return StandardScaler(
        inputCol=input_col,
        outputCol=output_col,
        withMean=True,
        withStd=True
    )
