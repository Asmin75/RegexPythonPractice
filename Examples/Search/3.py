"""
Write a Python program that matches a string that has
 an a followed by zero or more b's.
"""

import re

def text_match(string):
    pattern = 'ab*'
    if re.search(pattern, string):
        return 'Match found!'
    else:
        return 'Not matched!'


print(text_match("ac"))  # Match found!
print(text_match("bd"))  # Not matched!
print(text_match("ab"))  # Match found!
print(text_match("abbc"))  # Match found!



