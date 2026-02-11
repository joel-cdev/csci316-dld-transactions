from pyspark.ml.regression import LinearRegression
from pyspark.ml.regression import DecisionTreeRegressor


def train_linear_regression(train_df, feature_col, target_col):

    if "prediction" in train_df.columns:
        train_df = train_df.drop("prediction", "rawPrediction", "probability")  

    lr = LinearRegression(
        featuresCol=feature_col,
        labelCol=target_col
    )

    model = lr.fit(train_df)
    return model


def train_decision_tree(train_df, feature_col, target_col):
    
    if "prediction" in train_df.columns:
        train_df = train_df.drop("prediction", "rawPrediction", "probability")  

    dt = DecisionTreeRegressor(
        featuresCol=feature_col,
        labelCol=target_col,
        maxDepth=5
    )

    model = dt.fit(train_df)
    return model
