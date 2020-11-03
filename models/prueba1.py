#!/usr/bin/python3
""" Base Model Module """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize class base"""
        if kwargs:
            datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)
            if "__class__" in kwargs:
                del kwargs['__class__']
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            

    def __str__(self):
        """print the class name, id and directory"""
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))

    def save(self):
        """the current datetime"""
        self.updated_at = datetime.now()
        

    def to_dict(self):
        """returns a dictionary """
        base = self.__dict__.copy()
        base["created_at"] = self.created_at.isoformat()
        base["updated_at"] = self.updated_at.isoformat()
        base["__class__"] = self-__class__.__name__
        return base
