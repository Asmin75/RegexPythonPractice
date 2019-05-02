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


print(numbers_only("123450"))  # True
print(numbers_only("Ab345zij"))  # False
print(words_only("+123 1567 .^*90"))  # ['123', '1567', '90']
print(words_only("hello its me asmin"))  # ['hello', 'its', 'me', 'asmin']
print(alpha_numeric("abbreviation of water is h2o :) "))
# ['a', 'b', 'b', 'r', 'e', 'v', 'i',\ 'a', 't', 'i', \
# 'o', 'n', 'o', 'f', 'w', 'a', 't', 'e', 'r', 'i', 's', 'h', '2', 'o']
print(email_valid("asmin@gmail.com"))  # True
print(email_valid("asmin.rai7@gmail.com"))  # True
print(email_valid("asmin.rai7@com"))  # False


