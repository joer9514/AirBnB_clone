#!/usr/bin/python3
"""Class BaseModel"""

import json
import uuid
import models
from datetime import datetime

class BaseModel:
     """Constructor"""
     def __init__(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

     def __str__(self):
        """String Literal"""
        a, b, c = self.__class__.__name__, self.id, self.__dict__
        return("[{}] ({}) {}".format(a, b, c))

     def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

     def to_dict(self):
        """Returns a dictionay"""
        my_dict = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = item.isoformat()
            else:
                my_dict[key] = item
        my_dict['__class__'] = self.__class__.__name__
        return my_dict