import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")

find_match('^[0-9][0-9][^-].', 'a1a3', 1) # Y
find_match('^[a-z][0-9][^-].', 'a1a3w', 1) # Y
find_match('^[a-z][0-9][^-].', 'a1a', 1) # N (missing extra char for the period)
find_match('^[a-z][0-9][^-].', '11a3', 1) # N
find_match('^[a-z][0-9][^-].', 'aaa3', 1) # N
find_match('^[a-z][0-9][^-].', 'a1-3', 1) # N
