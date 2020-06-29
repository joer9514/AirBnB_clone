#!/usr/bin/python3
"""The console simulation"""

import cmd
import sys
import json
import models
import shlex
from models import amenity
from models.base_model import BaseModel
from models import city
from models import place
from models import state
from models import storage
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
    err_list =     err_list = ["** class name missing **", "** class doesn't exist **",
                    "** instance id missing **", "** no instance found **",]

    def err_msg(self, n):
        """Return error messages"""
        msg_dict = {1: "** class name missing **",
                    2: "** class doesn't exist **",
                    3: "** instance id missing **",
                    4: "** no instance found **",
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
    
    def do_show(self,line):
        """Print string representation of instance"""
        arg = line.split()
        if line == "":
            print(self.err_list[0])
        elif arg[0] not in self.group:
            print(self.err_list[1])
        elif len(arg) < 2:
            print(self.err_list[2])
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                object = data_dump[key]
                print(object)
            except KeyError:
                print(self.err_list[3])
      
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
