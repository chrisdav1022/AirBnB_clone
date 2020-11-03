#!/usr/bin/python3
"""json file"""
import models
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

class FileStorage():
    """class"""
    __file_path = 'file.json'
    self.__objects = {}

    def all(self):
        """return dictionary"""
        return self.__objects

    def new(self, obj):
        """obj class name id in object"""
        new = obj.class.__name__ + "." + obj.id
        self.__object[new] = obj


    def save(self):
        """save to objct"""
        nvd = {}
        with open(FileStorage.__file_path, 'w') as json:
            for key, value in self.__object,items():
                nvd[key] = value.to_dict()
            filejson.write(json.dumps(nvd))

    def reload(self):
        """reload json in the file object"""
        try:
            with open(fileStorage.__file_path, 'r') as json_r:
                rj = json.loads(json_r.read())
                for key, value in rj.item():
                    keysl = key.split(".")
                    nvd = globals()[keysl[0]](**value)
                    self.__object[key] = copy
        except IOError:
            return
