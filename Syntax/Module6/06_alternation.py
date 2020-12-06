import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")

#exact
find_match('abc|123', 'abcw', 1) # Y
find_match('abc|123', 'w123q', 2) # Y
find_match('abc|123', 'ab12', 3) # N
find_match('Yaniv', 'Hey Yaniv Nuriel', 4) # Y
