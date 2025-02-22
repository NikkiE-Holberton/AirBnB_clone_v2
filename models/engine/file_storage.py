#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            instance_list = {}
            for obj in FileStorage.__objects.keys():
                if cls.__name__ in obj:
                    instance_list[obj] = FileStorage.__objects[obj]
            return instance_list

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ delete object from objects dict """
        if obj is None:
            return
        elif obj in FileStorage.__objects.values():
            tmp_dict = FileStorage.__objects.copy()
            for key, val in tmp_dict.items():
                if val == obj:
                    FileStorage.__objects.pop(key)
        else:
            return

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = FileStorage.classes[
                            val[
                                '__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        self.reload()
