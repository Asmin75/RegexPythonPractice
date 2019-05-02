"""
Write a Python program that matches
a string that has an a followed by three 'b'.
"""

import re


def is_match(text):
    pattern = ("ab{3}")
    if re.search(pattern, text):
        return "Match found!"
    else:
        return "Match not found"


print(is_match("a"))