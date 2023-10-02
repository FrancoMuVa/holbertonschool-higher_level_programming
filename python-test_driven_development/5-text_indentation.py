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

    for i in range(len(text)):
        if text[i] in '.?:':
            print("{}".format(text[i]))
            print()

        elif (not (text[i] == " " and text[i - 1] in '.?:')) or i == 0:
            print("{}".format(text[i]), end="")
