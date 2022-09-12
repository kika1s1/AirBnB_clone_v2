#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
import models
from os import environ
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table


place_amenity_table = Table("place_amenity", Base.metadata, Column("place_id",
                    String(60), ForeignKey("places.id"), nullable=False),
                    Column("amenity_id", String(60),
                    ForeignKey("amenities.id"), nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary="place_amenity_table",
                                 viewonly=False)
