"""
MLFlow Run Create Module

Description:
    This module creates test run in MLFlow Server.
"""
from mlflow import MlflowClient


def create_run():
    # Create a client of MLFlow Tracking Server
    client = MlflowClient(tracking_uri="http://127.0.0.1:5000")

    # Create MLFlow run
    test_experiment = client.get_experiment_by_name(name="Test Experiment")

    run = client.create_run(
        experiment_id=test_experiment.experiment_id,
        tags={"Test Tag Key": "Test Tag Value"},
        run_name="Test Run",
    )

    # Print created run metadata info to check if run is created correctly
    print(f"Run tags: {run.data.tags}")
    print(f"Experiment ID: {run.info.experiment_id}")
    print(f"Run ID: {run.info.run_id}")
    print(f"Run Name: {run.info.run_name}")
    print(f"Lifecycle_stage: {run.info.lifecycle_stage}")
    print(f"Status: {run.info.status}")


if __name__ == "__main__":
    # Create run
    create_run()
