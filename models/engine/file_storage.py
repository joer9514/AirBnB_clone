"""Class File_storage"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class File_storage:
    """Private class attributes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary"""
        return File_storage.__objects

    def new(self, obj):
        """Return __objects with obj key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        save_file = self.__file_path
        new_dict = {}
        for key, item in self.__objects.items():
            new_dict[key] = item.to_dict()
        with open(save_file, "w", encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """JSON file to __objects"""
        reload_dict = {}
        try:
            with open(File_storage.__file_path, mode="r") as a_file:
                reload_dict = (json.load(a_file))
                for key, value in reload_dict.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
