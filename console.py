#!/usr/bin/python3
""" console based on cmd module """

import cmd

class HBNBCommand(cmd.Cmd):
    """ command interpreter with:
    quit and EOF to exit.
    help which is provided by default by cmd module
    """
    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """
        command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        command to exit the program after the EOF signal
        """
        return True

    def emptyline(self):
        """
        empty line don't execute anything
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
