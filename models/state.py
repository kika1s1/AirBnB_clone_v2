#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import environ
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            city_dict = models.storage.all(models.classes["City"])
            city_list = []

            for key, value in city_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
