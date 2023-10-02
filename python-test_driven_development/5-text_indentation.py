#!/usr/bin/python3
"""
    Function that prints a text with two new lines after a specific character.
"""


def text_indentation(text):
    """
        text_indentation: Take a text and prints it with new two lines after
        spesific characters: '.', '?' and ':'

        Args:
            text (str): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list = []
    line = ""
    for ch in text:
        line += ch
        if ch in '.?:':
            my_list.append(line.strip())
            line = ""
    
    for item in my_list:
        print("{}".format(item))
        print()