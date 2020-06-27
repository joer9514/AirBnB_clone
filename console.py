#!/usr/bin/python3
"""The console simulation"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
