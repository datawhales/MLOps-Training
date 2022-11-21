"""
Table Create module

Description:
    This module creates table in PostgreSQL DB.
"""
import psycopg2

from postgresql_training.meta import MyDB

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
    # Execute a SQL command (create table)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS iris_data (
            id serial PRIMARY KEY,
            sepal_length float8,
            sepal_width float8,
            petal_length float8,
            petal_width float8,
            target integer
        );"""
    )

    # Make the changes to the database persistent
    conn.commit()

conn.close()
