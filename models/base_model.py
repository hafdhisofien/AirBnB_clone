#!/usr/bin/python3
"""
This is our BaseModel class
"""

import models
from datetime import datetime
import uuid
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    An abstract class baseModel that defines all
    common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     time)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     time)
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
        Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
         updates the public instance attribute
         updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class
        converted to string object in ISO format.
        """
        iso_dict = dict(self.__dict__)
        iso_dict['__class__'] = type(self).__name__
        iso_dict['created_at'] = iso_dict['created_at'].isoformat()
        iso_dict['updated_at'] = iso_dict['updated_at'].isoformat()

        return iso_dict
