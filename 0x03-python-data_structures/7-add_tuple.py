#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = validate_tuple(tuple_a)
    j = validate_tuple(tuple_b)

    return ((i[0] + j[0]), (i[1] + j[1]))


def validate_tuple(_tpl=()):
    if len(_tpl) < 2:
        if len(_tpl) == 1:
            _tpl = (_tpl[0], 0)
        elif len(_tpl) == 0:
            _tpl = (0, 0)
    elif len(_tpl) > 2:
        _tpl = (_tpl[0], _tpl[1])

    return _tpl
