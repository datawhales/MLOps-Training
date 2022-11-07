"""
ML Model Load module

Description:
    This module loads the trained model from MLFlow Server.
"""
import os
import mlflow
from mlflow.client import MlflowClient
import pandas as pd
from sklearn.datasets import load_iris


def download_model():
    # Set MLFlow tracking uri
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    client = MlflowClient()

    # Get run info
    df = mlflow.search_runs(experiment_names=["Test Experiment"])

    # Get run_id
    run_id = df[df["tags.mlflow.runName"] == "Iris"]["run_id"].item()

    # Download model
    os.makedirs("download", exist_ok=True)
    download_path = client.download_artifacts(
        run_id=run_id,
        path="random-forest",
        dst_path="download",
    )

    print(f"Artifacts downloaded in: {download_path}")
    print(f"Artifacts: {os.listdir(download_path)}")


def load_model():
    # Load model
    model = mlflow.pyfunc.load_model(model_uri="download/random-forest")
    return model


def get_iris_sample():
    # Load iris dataset
    iris_dataset = load_iris()

    features = iris_dataset["data"]
    feature_names = ["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]

    feature_df = pd.DataFrame(features, columns=feature_names)
    return feature_df.sample(1)


if __name__ == "__main__":
    # Download model
    download_model()

    # Load model
    model = load_model()
    
    # Get sample data
    iris_sample = get_iris_sample()
    print(f"\nIris data sample:\n{iris_sample}")

    # Predict with loaded model
    pred = model.predict(iris_sample)
    print(f"\nPrediction: {pred}")
