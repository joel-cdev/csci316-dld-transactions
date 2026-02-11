from pyspark.ml.evaluation import RegressionEvaluator


def evaluate_model(model, test_df, feature_col, target_col):

    if "prediction" in test_df.columns:
        test_df = test_df.drop("prediction", "rawPrediction", "probability")  

    predictions = model.transform(test_df)

    evaluator_rmse = RegressionEvaluator(
        labelCol=target_col,
        predictionCol="prediction",
        metricName="rmse"
    )

    evaluator_r2 = RegressionEvaluator(
        labelCol=target_col,
        predictionCol="prediction",
        metricName="r2"
    )

    rmse = evaluator_rmse.evaluate(predictions)
    r2 = evaluator_r2.evaluate(predictions)

    return rmse, r2
