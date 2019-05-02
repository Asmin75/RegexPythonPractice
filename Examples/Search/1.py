# Search for the first white-space character in the string:

import re

a = "The rain in spain"
x = re.search("\s", a)

print(x)