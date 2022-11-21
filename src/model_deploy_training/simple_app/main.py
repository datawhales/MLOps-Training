from fastapi import FastAPI
import mlflow
import pandas as pd

from model_deploy_training.simple_app import schemas


# Create a FastAPI instance
app = FastAPI()

# Load model
MODEL = mlflow.pyfunc.load_model(model_uri="../model_registry_training/download/random-forest")


@app.post("/predict", response_model=schemas.PredictOut)
def predict(iris: schemas.PredictIn) -> schemas.PredictOut:
    df = pd.DataFrame([iris.dict()])
    pred = MODEL.predict(df).item()
    return schemas.PredictOut(iris_class=pred)
