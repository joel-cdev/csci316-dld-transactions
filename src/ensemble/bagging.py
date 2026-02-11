def ensemble_average(models, df):
    preds = [model.transform(df).select("prediction") for model in models]

    base = preds[0]
    for i in range(1, len(preds)):
        base = base.withColumnRenamed("prediction", f"pred_{i}")

    return base
