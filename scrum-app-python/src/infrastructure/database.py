from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os




user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
postgresserver = os.environ['DB_SERVER']
db = os.environ['POSTGRES_DB']

#SQLALCHEMY_DATABASE_URL = "sqlite:///scrum_task.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{postgresserver}/{db}"
#SQLALCHEMY_DATABASE_URL = f"postgresql://scrum:scrum@192.168.114.129:5432/scrum"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()