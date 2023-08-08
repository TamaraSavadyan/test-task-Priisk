from dataclasses import dataclass
import yaml


@dataclass
class DatabaseConfig:
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass
class Config:
    database: DatabaseConfig = None


def setup_config(config_path: str):
    with open(config_path, 'r') as file:
        raw_config = yaml.safe_load(file)

    return Config(
        database=DatabaseConfig(
            user=raw_config['database']['user'],
            password=raw_config['database']['password'],
            host=raw_config['database']['host'],
            port=raw_config['database']['port'],
            database=raw_config['database']['db'],
        ),
    )


config = setup_config('config.yaml')


if __name__ == '__main__':
    print(config)
