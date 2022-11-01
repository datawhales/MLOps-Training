import pandas as pd
from sqlalchemy import create_engine

from postgresql_training.meta import MyDB


class PGDataset:
    """
    PostgreSQL DB connection

    Description:
        This class reads data from postgresql db as dataframe using sqlalchemy.

    Attributes:
        user (str): An user name.
        password (str): A password.
        host (str): A host name.
        port (int): A port number.
        database (str): A database name.
        db (Engine): A sqlalchemy engine.
    """
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        # Create engine
        self.db = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    def read_data(self, sql_query: str) -> pd.DataFrame:
        """
        Read data from db

        Description:
            This module reads data from postgresql db.

        Args:
            sql_query (str): A sql query requested to db.

        Returns:
            (pd.DataFrame): A dataframe by query.
        """
        # DB connection
        with self.db.connect() as conn:
            df = pd.read_sql(sql=sql_query, con=conn)
        return df


if __name__ == "__main__":
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

    print(df)
