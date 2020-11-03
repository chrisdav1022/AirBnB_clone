#!/usr/bin/python3
""" Base Model Module """
import model
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize class base"""
        if kwargs:
            for keys, v in kwargs.items():
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """print the class name, id and directory"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary """
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new
