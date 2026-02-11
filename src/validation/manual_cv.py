from pyspark.ml.evaluation import RegressionEvaluator


def run_manual_cv(df, model_builder, feature_col, target_col, folds=10):

    df = df.withColumn("fold_id", (df["row_number"] % folds))

    evaluator = RegressionEvaluator(
        labelCol=target_col,
        predictionCol="prediction",
        metricName="rmse"
    )

    scores = []

    for fold in range(folds):

        train_df = df.filter(df.fold_id != fold)
        val_df = df.filter(df.fold_id == fold)

        model = model_builder(train_df)
        predictions = model.transform(val_df)

        rmse = evaluator.evaluate(predictions)
        scores.append(rmse)

    return scores
