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
            sepal_length_cm double precision,
            sepal_width_cm double precision,
            petal_length_cm double precision,
            petal_width_cm double precision,
            target integer
        );"""
    )

    # Make the changes to the database persistent
    conn.commit()

conn.close()
