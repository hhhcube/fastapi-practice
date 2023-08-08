from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
from fastapi import HTTPException

from src.config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME, DATABASE_PORT, DATABASE_NAME 

# Create a logger
logger = logging.getLogger(__name__)


SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# create function to create database session instance
def get_db():
    try:
        db = SessionLocal()

    except Exception as e:
       logger.error(f"An error occurred while creating the session: {e}")
       raise HTTPException(status_code=500, detail="Could not connect to the database")

    try:
        yield db
    except Exception as e:
        logger.error(f"An error occurred while handling the session: {e}")
        raise    
    finally:
        db.close()





# Raw SQL
# while True:

#     try: 
#         conn = psycopg2.connect(host='localhost', database='fastapi, user='postgres',
#                                 password='abc123', cursor_factory=RealDictCursor)
#         conn = conn.cursor()
#         print("Dtabase connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

