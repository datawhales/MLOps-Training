from meta import MyDB

import pandas as pd
import psycopg2
from sklearn.datasets import load_iris
import time

# Load iris dataset
iris_dataset = load_iris()
features, labels = iris_dataset["data"], iris_dataset["target"]
feature_names = ["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]
label_names = ["target"]

feature_df = pd.DataFrame(features, columns=feature_names)
label_df = pd.DataFrame(labels, columns=label_names)

df = pd.concat([feature_df, label_df], axis=1)


def data_generator(df: pd.DataFrame):
    """
    Data generator
    """
    idx = 0
    while idx < len(df):
        yield tuple(df.iloc[idx].values)
        idx += 1


gen = data_generator(df)

while True:
    # Connect to an existing database
    conn = psycopg2.connect(
        database=MyDB.database,
        user=MyDB.user,
        password=MyDB.password,
        host=MyDB.host,
        port=MyDB.port,
    )

    try:
        data_row = next(gen)
    except StopIteration:
        gen = data_generator(df)
        data_row = next(gen)

    # Open a cursor to perform database operations
    with conn.cursor() as cursor:
        # Execute a SQL command (insert rows continuously)     
        cursor.execute(
            """INSERT INTO iris_data (
                sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm, target
            ) VALUES (%s, %s, %s, %s, %s)""", data_row
        )

        time.sleep(5)

        # Make the changes to the database persistent
        conn.commit()

    conn.close()
