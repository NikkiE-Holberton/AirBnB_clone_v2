#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, null
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    __tablename__ = 'users'

    places = relationship(
        "Place",
        cascade="all,
        delete-orphan",
        backref='user')
    reviews = relationship(
        "Review",
        cascade="all,
        delete-orphan",
        backref='user')
