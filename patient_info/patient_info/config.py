import os


class Config:
    secret_key = os.getenv("SECRET_KEY")
    debug = os.getenv("DEBUG", True)

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT", 5432)


config = Config()
