#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None
    else:
        best_score_key = ""
        best_score_value = 0
        for name, score in a_dictionary.items():
            if best_score_value == 0:
                best_score_value = score
                best_score_key = name
            elif score > best_score_value:
                best_score_value = score
                best_score_key = name
            else:
                pass
    return best_score_key
