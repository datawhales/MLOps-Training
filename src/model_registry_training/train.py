"""
ML Model Training module

Description:
    This module trains the model for iris data with logging to MLFlow Server.
    Also the module saves the model to MLFlow Server.
"""
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, precision_recall_fscore_support

from model_registry_training.export_data import PGDataset
from postgresql_training.meta import MyDB


def get_data():
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
    return df


def train(df):
    # Define X, y
    X = df.drop(["id", "target"], axis=1)
    y = df["target"]

    # Split train data and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    print(f"Train data num: {len(X_train)}")
    print(f"Test data num: {len(X_test)}")

    # Set MLFlow tracking uri
    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    # Start run - model training & model logging
    with mlflow.start_run(experiment_id=1, run_name="Iris", description="Iris Data Training"):
        params = {
            "n_estimators": 100,
            "random_state": 42,
        }

        # Parameters logging
        mlflow.log_params(params)

        # Model training
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        # Model predict
        y_pred = model.predict(X_test)
        score = round(precision_recall_fscore_support(y_test, y_pred, average='weighted')[2], 4)
        print("\n=============== Random Forest ===============")
        print(classification_report(y_test, y_pred))
        print(f"Weighted avg f1-score: {score}")

        # Metrics logging
        mlflow.log_metric(
            key="weighted_f1_score",
            value=score,
        )

        # Model logging
        mlflow.sklearn.log_model(model, artifact_path="random-forest")


if __name__ == "__main__":
    # Get data from db
    df = get_data()

    # Model training
    train(df=df)
