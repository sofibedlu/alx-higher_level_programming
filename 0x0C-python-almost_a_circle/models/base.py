#!/usr/bin/python3
"""Define the Base class"""
import json
import csv


class Base:
    """the base class of other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the instance
        Args:
            id: id of an instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representations of list of dictionaries
        Args:
            list_dictionaries (list): list of dictinaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list of objects to file
        Args:
            list_objs (list): list of instances that inherits of Base class
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_o = []
                for ins in list_objs:
                    list_o.append(ins.to_dictionary())
                f.write(Base.to_json_string(list_o))

    @staticmethod
    def from_json_string(json_string):
        """return the list of objects from list JSON string representation
        Args:
            json_string (str): a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set
        Args:
            **dictionary: keyword argument representation of a dictionary
        """
        if bool(dictionary):
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                j_string = f.read()
        except FileNotFoundError:
            return []
        obj_list = Base.from_json_string(j_string)
        return [cls.create(**inst) for inst in obj_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes or (serializes) a data in csv format

        Args:
            list_objs (list): list of instances
        """

        filename = cls.__name__ + '.csv'
        if cls.__name__ == "Rectangle":
            fieldname = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldname = ["id", "size", "x", "y"]
        with open(filename, 'w', newline='') as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
            else:
                csvwriter = csv.DictWriter(csv_f, fieldnames=fieldname)
                dics = [obj.to_dictionary() for obj in list_objs]
                for row in dics:
                    csvwriter.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """reads or (deserializes) from csv file
            return list of instances
        """

        filename = cls.__name__ + '.csv'
        if cls.__name__ == "Rectangle":
            fieldname = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldname = ["id", "size", "x", "y"]
        try:
            with open(filename, 'r', newline='') as csv_f:
                csv_reader = csv.DictReader(csv_f, fieldnames=fieldname)
                list_dicts = [{k: int(v) for k, v in row.items()}
                              for row in csv_reader]
                return [cls.create(**obj) for obj in list_dicts]
        except FileNotFoundError:
            return []
