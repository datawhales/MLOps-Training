from meta import MyDB

from sklearn.datasets import load_iris
import pandas as pd
import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
    database=MyDB.database,
    user=MyDB.user,
    password=MyDB.password,
    host=MyDB.host,
    port=MyDB.port,
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Load iris dataset
iris_dataset = load_iris()
features, labels = iris_dataset["data"], iris_dataset["target"]
feature_names = ["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]
label_names = ["target"]

feature_df = pd.DataFrame(features, columns=feature_names)
label_df = pd.DataFrame(labels, columns=label_names)

df = pd.concat([feature_df, label_df], axis=1)

# Execute a SQL command (insert row)
cur.execute(
    """INSERT INTO iris_data (
        sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm, target
    ) VALUES (%s, %s, %s, %s, %s)""", tuple(df.iloc[0].values)
)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
