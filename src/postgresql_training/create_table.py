from meta import MyDB

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

# Execute a SQL command (create table)
cur.execute(
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

# Close communication with the database
cur.close()
conn.close()
