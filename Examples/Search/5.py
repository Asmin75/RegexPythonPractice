"""
Write a Python program that matches
a string that has an a followed by two to three 'b'
"""

import re


def is_matched(text):
    patterns = ("ab{2,3}")
    if re.search(patterns,text):
        return "Match Found!"
    else:
        return "Match does not found"


print(is_matched("ab"))  # Match does not found
print(is_matched("abb"))  # Match found
print(is_matched("abbb"))  # Match found
print(is_matched("abbbb"))  # Match found

