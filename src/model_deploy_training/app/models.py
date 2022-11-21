from model_deploy_training.app.database import Base

from sqlalchemy import Column, Integer, DateTime, Float


class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)


class Prediction(Base):
    __tablename__ = "prediction"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    iris_class = Column(Integer)
