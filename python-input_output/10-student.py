#!/usr/bin/python3
"""
    Clas Student
"""


class Student():
    """ Class Student that defines a student  """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new instance of Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student """
        if not isinstance(attrs, list):
            return self.__dict__

        students_dict = {}
        for item in attrs:
            if item in self.__dict__:
                students_dict[item] = self.__dict__[item]

        return students_dict
