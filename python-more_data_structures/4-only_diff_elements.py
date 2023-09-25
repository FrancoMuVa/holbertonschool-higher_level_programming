#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for item_1 in set_1:
        if item_1 not in set_2:
            new_set.add(item_1)

    for item_2 in set_2:
        if item_2 not in set_1:
            new_set.add(item_2)
    return new_set
