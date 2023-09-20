#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    leng = len(cpy_list)
    if idx < 0 or idx > leng - 1:
        return cpy_list
    cpy_list[idx] = element
    return cpy_list
