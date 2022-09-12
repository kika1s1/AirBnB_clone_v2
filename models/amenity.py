#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
