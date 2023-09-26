#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = list(a_dictionary.values())[0]
    retu_key = list(a_dictionary.keys())[0]
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            retu_key = key
    return retu_key
