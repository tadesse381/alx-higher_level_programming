#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for a, b in a_dictionary.items():
        if b == value:
            keys.append(a)

    for a in keys:
        del a_dictionary[a]

    return a_dictionary
