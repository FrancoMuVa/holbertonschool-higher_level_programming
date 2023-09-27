#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None

    rom_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    for letter in roman_string:
        if letter not in rom_dic:
            return sum

    for j in range(len(roman_string)):
        for key, val in rom_dic.items():
            if j + 1 < len(roman_string):
                if roman_string[j] == key and val < rom_dic[roman_string[j+1]]:
                    sum -= val
                elif roman_string[j] == key:
                    sum += val
            else:
                if roman_string[j] == key:
                    sum += val
    return sum
