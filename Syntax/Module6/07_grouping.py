import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")

#+ means once or more
find_match('(abc)+', 'abcw', 1) # Y
find_match('(abc)+', 'wabcabc', 2) # Y
find_match('(abc)+', 'abwab', 3) # N
