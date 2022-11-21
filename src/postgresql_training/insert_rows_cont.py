"""
Streaming Data Insert module

Description:
    This module inserts data periodically into table in postgreSQL DB.
"""
import pandas as pd
import psycopg2
from sklearn.datasets import load_iris
import time

from postgresql_training.meta import MyDB

# Load iris dataset
iris_dataset = load_iris()
features, labels = iris_dataset["data"], iris_dataset["target"]
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
label_names = ["target"]

feature_df = pd.DataFrame(features, columns=feature_names)
label_df = pd.DataFrame(labels, columns=label_names)

df = pd.concat([feature_df, label_df], axis=1)


def data_generator(df: pd.DataFrame):
    """
    Data generator
    """
    idx = 0
    while True:
        yield tuple(df.iloc[idx].values)
        idx += 1
        idx %= len(df)


gen = data_generator(df)

# Connect to an existing database
conn = psycopg2.connect(
    database=MyDB.database,
    user=MyDB.user,
    password=MyDB.password,
    host=MyDB.host,
    port=MyDB.port,
)

while True:
    data_row = next(gen)

    # Open a cursor to perform database operations
    with conn.cursor() as cursor:
        # Execute a SQL command (insert rows continuously)     
        cursor.execute(
            """INSERT INTO iris_data (
                sepal_length, sepal_width, petal_length, petal_width, target
            ) VALUES (%s, %s, %s, %s, %s)""", data_row
        )

        time.sleep(5)

        # Make the changes to the database persistent
        conn.commit()

conn.close()
