#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """it retrieves a dictionary representation of a Student instance
        Args:
        attrs (list): list of strings(keys to the dictionary)
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            dic = vars(self)
            new_dic = {}
            for key in attrs:
                try:
                    dic[key]
                except KeyError:
                    continue
                new_dic[key] = dic[key]
            return new_dic
        return vars(self)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json (dict): dictionary object from json file
        """
        if type(json) == dict and bool(json):
            self.__dict__ = json
