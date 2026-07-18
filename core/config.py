from dataclasses import dataclass


@dataclass
class DatabaseConfig:

    host: str = "localhost"

    user: str = "root"

    password: str = ""

    database: str = "search_db"

    port: int = 3306


DATABASE = DatabaseConfig()


@dataclass
class TornadoConfig:

    host: str = "0.0.0.0"

    port: int = 8889


TORNADO = TornadoConfig()