import os
import sys
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import datetime
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname =  Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    profile_picture_url = Column(String)
    bio =  Column(String(300))
    created_at =  Column(DateTime)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.timezone.utc)
    user_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    user = relationship("User")

class Media(Base):
    __tablename__ = 'media'
    
    ID = Column(Integer, primary_key=True)
    type = Column(Enum('image', 'video', name="media_type"), nullable=False)
    url = Column(String(255), nullable=False)
    size = Column(Integer)
    format = Column(String(50))
    post_id = Column(Integer, ForeignKey('post.ID'))
    
    post = relationship("Post")

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    comment_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.timezone.utc)
    author_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.ID'), nullable=False)
   
    user = relationship("User")
    post = relationship("Post",)

class Reaction(Base):
    __tablename__ = 'reaction'

    ID = Column(Integer, primary_key=True)
    type = Column(Enum('like', 'love', 'hahaha', 'wow', 'sad', 'angry', name="reaction_type"))
    user_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.ID'), nullable=False)

    user = relationship("User")
    post = relationship("Post")

class Follower(Base):
    __tablename__ = 'follower'
    
    user_from_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
     


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
