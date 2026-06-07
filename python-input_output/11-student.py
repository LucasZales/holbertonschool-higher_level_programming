#!/usr/bin/python3
"""Class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            result = {}
            for key in attrs:
                if isinstance(key, str) and key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
