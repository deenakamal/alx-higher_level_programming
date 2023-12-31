#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    result = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    idx = 0
    while idx < len(roman_string):
        current_value = d[roman_string[idx]]
        if idx > 0 and current_value > d[roman_string[idx - 1]]:
            result += current_value - 2 * d[roman_string[idx - 1]]

        else:
            result += current_value
        idx += 1
    return result
