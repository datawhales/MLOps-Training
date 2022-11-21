"""
Data Insert module

Description:
    This module inserts data into table in postgresQL DB.
"""
import pandas as pd
import psycopg2
from sklearn.datasets import load_iris

from postgresql_training.meta import MyDB

# Load iris dataset
iris_dataset = load_iris()
features, labels = iris_dataset["data"], iris_dataset["target"]
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
label_names = ["target"]

feature_df = pd.DataFrame(features, columns=feature_names)
label_df = pd.DataFrame(labels, columns=label_names)

df = pd.concat([feature_df, label_df], axis=1)

# Connect to an existing database
conn = psycopg2.connect(
    database=MyDB.database,
    user=MyDB.user,
    password=MyDB.password,
    host=MyDB.host,
    port=MyDB.port,
)

# Open a cursor to perform database operations
with conn.cursor() as cursor:
    # Execute a SQL command (insert row)
    cursor.execute(
        """INSERT INTO iris_data (
            sepal_length, sepal_width, petal_length, petal_width, target
        ) VALUES (%s, %s, %s, %s, %s)""", tuple(df.iloc[0].values)
    )

    # Make the changes to the database persistent
    conn.commit()

conn.close()
