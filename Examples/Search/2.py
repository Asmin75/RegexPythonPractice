"""
Write a Python program to check that a
string contains only a certain set of characters
 (in this case a-z, A-Z and 0-9).
 """


import re


def is_allowed(string):
    charRe = re.compile(r'[a-zA-Z0-9.]')
    string = charRe.search(string)
    return bool(string)


print(is_allowed("ABCDEFabcdef123450"))
print(is_allowed("*&^%"))