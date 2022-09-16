#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = 0
    for clave in a_dictionary:
        if a_dictionary[clave] > biggest:
            biggest = a_dictionary[clave]
            score = clave
    return score
