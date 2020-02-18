#!/usr/bin/python3
"""
file storage class
"""
import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_json = {}
        for key, val in self.__objects.items():
            obj_json[key] = val.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_json, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as f:
                loader = json.load(f)
            for key in loader:
                self.__objects[key] = classes[loader[key]
                                              ["__class__"]](**loader[key])
        except:
            pass
