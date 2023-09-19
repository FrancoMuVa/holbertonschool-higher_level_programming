#!/usr/bin/python3
def remove_char_at(str, n):
    i = -1
    for char in str:
        i += 1
        if i == n:
            str = str.replace(char, "")
    return (str)
