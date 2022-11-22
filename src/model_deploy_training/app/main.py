from datetime import datetime
from fastapi import Depends, FastAPI
import mlflow
import pandas as pd
from sqlalchemy.orm import Session

from model_deploy_training.app.database import SessionLocal, engine
from model_deploy_training.app.models import Base, RawData, Prediction
from model_deploy_training.app.schemas import PredictIn, PredictOut

Base.metadata.create_all(bind=engine)

# Create a FastAPI instance
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Load model
MODEL = mlflow.pyfunc.load_model(model_uri="../model_registry_training/download/random-forest")


@app.post("/predict", response_model=PredictOut)
def predict(iris: PredictIn, db: Session = Depends(get_db)) -> PredictOut:
    # Predict
    df = pd.DataFrame([iris.dict()])
    pred = MODEL.predict(df).item()

    # Get timestamp
    now = datetime.utcnow()
    
    raw_data = RawData(timestamp=now, **iris.dict())
    db.add(raw_data)
    db.commit()
    db.refresh(raw_data)

    prediction = Prediction(timestamp=now, iris_class=pred)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return PredictOut(iris_class=pred)


@app.get("/predict/", response_model=PredictOut)
def get_prediction(sepal_length, sepal_width, petal_length, petal_width, db: Session = Depends(get_db)) -> PredictOut:
    data_row = db.query(RawData).filter(RawData.sepal_length == sepal_length) \
                     .filter(RawData.sepal_width == sepal_width) \
                     .filter(RawData.petal_length == petal_length) \
                     .filter(RawData.petal_width == petal_width) \
                     .first()

    pred_row = db.query(Prediction).filter(Prediction.timestamp == data_row.timestamp).first()

    return PredictOut(iris_class=pred_row.iris_class)
