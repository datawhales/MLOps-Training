from dataclasses import dataclass


@dataclass
class MyDB:
    """
    My Database information

    Description:
        This data class specifies the connection URL information of my database.

    Attributes:
        database (str): A database name.
        user (str): An user name.
        password (str): A password.
        host (str): A host name.
        port (int): A port number.
    """

    database: str = "mydatabase"
    user: str = "postgres"
    password: str = "mypassword"
    host: str = "localhost"
    port: int = 5432
