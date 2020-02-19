#!/usr/bin/python3
""" console based on cmd module """

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "State": State,
           "City": City, "Amenity": Amenity, "Review": Review}


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
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif args[0] in classes:
                key = args[0] + "." + args[1]
                try:
                    models.storage.all()[key]
                    models.storage.all().pop(key)
                    models.storage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        all_obj = []
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in models.storage.all().items():
            if len(args) != 0:
                if type(val) is eval(args):
                    all_obj.append(str(val))
            else:
                all_obj.append(str(val))

        print(all_obj)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = models.storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
