#  Every model represents a table in our database
# import sys
# sys.path.append('C:/Users/Humphrey Hills/Documents/Python-scripts/chato-gazoo/')

from .database import Base

from sqlalchemy.sql.expression import text
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from sqlalchemy.sql.expression import text
# ---------------------------------------------------------------




class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    
    # Create a relationship with User table using the model name "User" not the table name "users" returns class properties except password
    owner = relationship("User") 




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, 
                primary_key=True, 
                nullable=False)

    email = Column(String, 
                   nullable=False, 
                   unique=True)

    password = Column(String, 
                      nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, 
                        server_default=text('now()'))

    phone_number = Column(String)

class Votes(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), 
        primary_key=True)
    
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), 
        primary_key=True)

