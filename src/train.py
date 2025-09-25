import mlflow
import mlflow.sklearn
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib
import os

DATA_PATH = "data/icecream_sales.csv"
MODEL_PATH = "models/linear_regression.joblib"

def main():
    df = pd.read_csv(DATA_PATH)
    X = df[["temperatura"]]
    y = df["vendas"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    mlflow.set_experiment("Gelato_Magico_Experiment")
    with mlflow.start_run() as run:
        mlflow.log_param("model", "LinearRegression")
        mlflow.log_param("feature", "temperatura")
        mlflow.log_metric("rmse", float(rmse))
        mlflow.log_metric("r2", float(r2))
        mlflow.sklearn.log_model(model, "model")

        os.makedirs("models", exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        mlflow.log_artifact(MODEL_PATH)

        print("Run id:", run.info.run_id)
        print("RMSE:", rmse)
        print("R2:", r2)

if __name__ == "__main__":
    main()
