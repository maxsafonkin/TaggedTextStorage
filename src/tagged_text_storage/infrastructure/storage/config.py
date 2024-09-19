from dataclasses import InitVar, dataclass, field


@dataclass
class StorageConfig:
    ip: InitVar[str]
    port: InitVar[int]
    user: InitVar[str]
    password: InitVar[str]
    db_name: InitVar[str]

    conn_uri: str = field(init=False)

    def __post_init__(self, ip: str, port: int, user: str, password: str, db_name: str) -> None:
        self.conn_uri = f"postgresql+psycopg2://{user}:{password}@{ip}:{port}/{db_name}"
