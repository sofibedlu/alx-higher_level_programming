#!/usr/bin/python3
"""Class Student module"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """it retrieves a dictionary representation of a Student instance
        """
        return vars(self)
