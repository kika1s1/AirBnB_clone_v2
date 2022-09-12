#!/usr/bin/python3
"""
Storage module
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
import models
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class_list = [City, State, User, Place, Review]


class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        init method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        current database session query
        """
        new_dict = {}

        if not cls:
            for a_class in class_list:
                for obj in self.__session.query(a_class):
                    k = obj.__class__.__name__, obj.id
                    new_dict[k] = obj
        else:
            if type(cls) is str:
                cls = models.classes[cls]
            query = self.__session.query(cls)
            for obj in query:
                k = obj.__class__.__name__, obj.id
                new_dict[k] = obj
        return new_dict

    def new(self, obj):
        """
        add object to current session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        creates all tables
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        close session
        """
        self.__session.remove()
