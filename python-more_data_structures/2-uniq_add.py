#!/usr/bin/python3
def uniq_add(my_list=[]):
    aux_list = []
    sum = 0
    for i in my_list:
        if i not in aux_list:
            aux_list.append(i)
            sum += i
    return sum
