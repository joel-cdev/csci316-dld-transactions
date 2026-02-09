from pyspark.ml.evaluation import RegressionEvaluator


def get_rmse_evaluator(label_col="meter_sale_price",
                       prediction_col="prediction"):
    """
    Create an RMSE evaluator.
    """
    return RegressionEvaluator(
        labelCol=label_col,
        predictionCol=prediction_col,
        metricName="rmse"
    )
