import re


def numbers_only(string):
    patterns = r'^\d+$'
    if re.search(patterns, string):
        return True
    else:
        return False


def words_only(string):
    patterns = r'\w+'
    list1 = re.findall(patterns, string)
    return list1


def alpha_numeric(string):
    patterns = r'[a-zA-Z0-9]'
    list1 = re.findall(patterns, string)
    return list1


def email_valid(string):
    patterns = r'[\w.%_-]+@[\w.-]+\.[a-zA-Z]{2,3}'
    if re.search(patterns, string):
        return True
    else:
        return False