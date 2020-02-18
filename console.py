#!/usr/bin/python3
""" console based on cmd module """

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel}


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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if args[0] in classes:
                key = args[0] + "." + args[1]
                try:
                    value = models.storage.all()[key]
                    print(value)
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        if args[0] in classes:
                key = args[0] + "." + args[1]
                try:
                    models.storage.all()[key]
                    models.storage.all().pop(key)
                    models.storage.save()
                except KeyError:                                                                                                            print("** no instance found **")
        elif args[0] not in classes:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = shlex.split(args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
