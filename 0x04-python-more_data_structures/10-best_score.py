#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    items = [(v, k) for k, v in a_dictionary.items()]
    b_score = max(items, key=lambda x: x[0], default=None)
    return b_score[1] if b_score is not None else None
