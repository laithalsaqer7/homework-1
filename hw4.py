# return the number of occurrences for each character inside of string and put it inside a dictionary

from collections import Counter

def count_characters_no_spaces(s):
    return dict(Counter(s.replace(" ", "")))

string = "Respect for you"
result = count_characters_no_spaces(string)


for char, count in result.items():
    print(f"'{char}': {count}")