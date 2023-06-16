#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    rmn_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    numb = 0
    lst = 0

    for letter in roman_string:
        for element in rmn_letter:
            if letter == elem[0]:
                if lst == 0 or last >= element[1]:
                    numb += element[1]
                elif lst < element[1]:
                    numb += element[1] - (last * 2)

                lst = element[1]

    return numb
