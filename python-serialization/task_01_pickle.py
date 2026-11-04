#!/usr/bin/python3
"""
Custom object serialization using pickle.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)

            if not isinstance(obj, cls):
                return None

            return obj

        except (OSError, pickle.PickleError, EOFError, AttributeError,
                ImportError, IndexError, TypeError, ValueError):
            return None
