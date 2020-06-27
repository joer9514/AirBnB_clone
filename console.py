#!/usr/bin/python3
"""The console simulation"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = '(hbnb) '
    classes = {"user",
               "BaseModel",
               "place",
               "State",
               "Amenity",
               "City",
               "Review"}

    def do_EOF(self, inputline):
        """Exit console"""
        return True

    def do_quit(self, inputline):
        """Quit command to exit console"""
        return True

    def do_create(self, args):
        """Create a new instance of a class and prints the id"""
        pass

    def do_show(self, args):
        """ Prints the json file of an instance of a class name and id """
        pass

    def do_all(self, args):
        """ Prints all string representation of all instances """
        pass

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        pass

    def do_update(self, args):
        """ Updates an instance"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
