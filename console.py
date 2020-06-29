#!/usr/bin/python3
"""The console simulation"""

import cmd
import sys
import json
import shlex
from models import amenity
from models.base_model import BaseModel
from models import city
from models import place
from models import state
from models import review
from models.user import User



class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = ' start (hbnb) '
    group = {"user",
               "BaseModel",
               "place",
               "State",
               "Amenity",
               "City",
               "Review"}
    

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on console"""
        return True
    err_list = ["** class name missing **", "** class doesn't exist **"]

    def err_msg(self, n):
        """Return error messages"""
        msg_dict = {1: "** class name missing **",
                    2: "** class doesn't exist **",
                    }
        for key, item in msg_dict.items():
            if key == n:
                print(item)

    def do_create(self, arg):
        """Used to create a new instance of BaseModel and saves
        the instance to a JSON file"""
        if arg == "":
            print(self.err_list[0])
        elif arg not in self.group:
            print(self.err_list[1])
        else:
            arg = eval(arg)()
            arg.save()
            print(arg.id)
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
