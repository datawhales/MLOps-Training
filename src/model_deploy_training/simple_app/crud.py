from fastapi import FastAPI
import mlflow
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

from model_deploy_training.simple_app import schemas


# Create a FastAPI instance
app = FastAPI()

# Load model
model = mlflow.pyfunc.load_model(model_uri="../model_registry_training/download/random-forest")

# Load iris dataset
iris_dataset = load_iris()

features = iris_dataset["data"]
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
df = pd.DataFrame(features, columns=feature_names)

# Get sample data
iris_sample = df.sample(1)

# Predict with loaded model
pred = model.predict(iris_sample).item()


@app.post("/predict", response_model=schemas.PredictOut)
def predict(iris: schemas.PredictIn) -> schemas.PredictOut:
    input_array = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    pred = model.predict(input_array)
    return schemas.PredictOut(iris_class=pred.item())
