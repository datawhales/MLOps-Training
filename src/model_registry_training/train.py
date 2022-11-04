"""
ML Model Training module

Description:
    This module trains the model for iris data with logging to MLFlow Server.
    Also the module saves the model to MLFlow Server.
"""
from pathlib import Path
import numpy as np
import mlflow
from mlflow.client import MlflowClient
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, precision_recall_fscore_support

from model_registry_training.export_data import PGDataset
from postgresql_training.meta import MyDB

# Setup database connection
pgdataset = PGDataset(
    user=MyDB.user,
    password=MyDB.password,
    host=MyDB.host,
    port=MyDB.port,
    database=MyDB.database,
)

# Read data from db
df = pgdataset.read_data(sql_query="SELECT * FROM iris_data ORDER BY id DESC LIMIT 100;")

# Define X, y
X = np.array(df[["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]])
y = np.array(df["target"])

# Split train data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print(f"Train data num: {len(X_train)}")
print(f"Test data num: {len(X_test)}")

# Set MLFlow tracking uri
mlflow.set_tracking_uri("http://127.0.0.1:5001")

client = MlflowClient()

# Create Experiment in MLFlow server
experiment_id = client.create_experiment(
    name="Iris Data",
    artifact_location=Path.cwd().joinpath("mlruns").as_uri(),
    tags={"version": "v1", "priority": "P1"},
)

# Print created experiment metadata info
print("\n=============== Experiment Created ===============")
experiment = client.get_experiment(experiment_id)
print(f"Experiment Name: {experiment.name}")
print(f"Experiment ID: {experiment.experiment_id}")
print(f"Artifact Location: {experiment.artifact_location}")
print(f"Experiment Tags: {experiment.tags}")
print(f"Lifecycle_stage: {experiment.lifecycle_stage}")

# Create Run in MLFlow server
run = client.create_run(
    experiment_id=experiment_id,
    tags={"Model Algorithm": "Random Forest"},
    run_name="run-1",
)

# Print created run metadata info
print("\n=============== Run Created ===============")
print(f"Run tags: {run.data.tags}")
print(f"Experiment ID: {run.info.experiment_id}")
print(f"Run ID: {run.info.run_id}")
print(f"Run Name: {run.info.run_name}")
print(f"Lifecycle_stage: {run.info.lifecycle_stage}")
print(f"Status: {run.info.status}")

# Start run - model training & model logging
with mlflow.start_run(run_id=run.info.run_id, experiment_id=experiment_id):
    params = {
        "n_estimators": 100,
        "random_state": 42,
    }
    mlflow.log_params(params)

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\n=============== Random Forest 1 ===============")
    print(classification_report(y_test, y_pred))
    print(f"Weighted avg f1-score: {precision_recall_fscore_support(y_test, y_pred, average='weighted')[2]:.4f}")

    mlflow.log_metric(
        key="weighted_f1_score",
        value=round(precision_recall_fscore_support(y_test, y_pred, average='weighted')[2], 4),
    )

    mlflow.sklearn.log_model(model, artifact_path="random-forest-1")

# Create Run in MLFlow server
run = client.create_run(
    experiment_id=experiment_id,
    tags={"Model Algorithm": "Random Forest"},
    run_name="run-2",
)

# Print created run metadata info
print("\n=============== Run Created ===============")
print(f"Run tags: {run.data.tags}")
print(f"Experiment ID: {run.info.experiment_id}")
print(f"Run ID: {run.info.run_id}")
print(f"Run Name: {run.info.run_name}")
print(f"Lifecycle_stage: {run.info.lifecycle_stage}")
print(f"Status: {run.info.status}")

# Start run - model training & model logging
with mlflow.start_run(run_id=run.info.run_id, experiment_id=experiment_id):
    params = {
        "n_estimators": 100,
        "random_state": 43,
    }
    mlflow.log_params(params)

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\n=============== Random Forest 2 ===============")
    print(classification_report(y_test, y_pred))
    print(f"Weighted avg f1-score: {precision_recall_fscore_support(y_test, y_pred, average='weighted')[2]:.4f}")

    mlflow.log_metric(
        key="weighted_f1_score",
        value=round(precision_recall_fscore_support(y_test, y_pred, average='weighted')[2], 4),
    )

    mlflow.sklearn.log_model(model, artifact_path="random-forest-2")

# Create Run in MLFlow server
run = client.create_run(
    experiment_id=experiment_id,
    tags={"Model Algorithm": "Random Forest"},
    run_name="run-3",
)

# Print created run metadata info
print("\n=============== Run Created ===============")
print(f"Run tags: {run.data.tags}")
print(f"Experiment ID: {run.info.experiment_id}")
print(f"Run ID: {run.info.run_id}")
print(f"Run Name: {run.info.run_name}")
print(f"Lifecycle_stage: {run.info.lifecycle_stage}")
print(f"Status: {run.info.status}")

# Start run - model training & model logging
with mlflow.start_run(run_id=run.info.run_id, experiment_id=experiment_id):
    params = {
        "n_estimators": 100,
        "random_state": 44,
    }
    mlflow.log_params(params)

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\n=============== Random Forest 3 ===============")
    print(classification_report(y_test, y_pred))
    print(f"Weighted avg f1-score: {precision_recall_fscore_support(y_test, y_pred, average='weighted')[2]:.4f}")

    mlflow.log_metric(
        key="weighted_f1_score",
        value=round(precision_recall_fscore_support(y_test, y_pred, average='weighted')[2], 4),
    )

    mlflow.sklearn.log_model(model, artifact_path="random-forest-3")
