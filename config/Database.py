from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from utils.settings import Settings

settings = Settings()


DATABASE = settings.db_name
PASSWORD_DB = settings.db_password
HOST_DB = settings.db_host
USERNAME_DB = settings.db_username
PORT_DB = settings.db_port

URI = (
    "mysql+pymysql://"
    + USERNAME_DB
    + ":"
    + PASSWORD_DB
    + "@"
    + HOST_DB
    + ":"
    + PORT_DB
    + "/"
    + DATABASE
)

# Create Database Engine
engine = create_engine(URI, pool_pre_ping=True, pool_recycle=3600)

SessionLocal = Session(engine)


# Functions to generate database connections
def get_db_connection():
    try:
        yield SessionLocal
    except InvalidRequestError:
        SessionLocal.rollback()
        raise
    finally:
        SessionLocal.close()


BaseModel = declarative_base()
