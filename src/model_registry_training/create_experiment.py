"""
MLFlow Experiment Create Module

Description:
    This module creates test experiment in MLFlow Server.
"""
from pathlib import Path
from mlflow import MlflowClient

# Create a client of MLFlow Tracking Server
client = MlflowClient(tracking_uri="http://127.0.0.1:5001")

# Create MLFlow experiment
experiment_id = client.create_experiment(
    name="Test Experiment",
    artifact_location=Path.cwd().joinpath("mlruns").as_uri(),
    tags={"version": "v0", "priority": "P0"},
)

# Fetch experiment metadata information to check if experiment is created correctly
experiment = client.get_experiment(experiment_id)
print(f"Experiment Name: {experiment.name}")
print(f"Experiment ID: {experiment.experiment_id}")
print(f"Artifact Location: {experiment.artifact_location}")
print(f"Experiment Tags: {experiment.tags}")
print(f"Lifecycle_stage: {experiment.lifecycle_stage}")
