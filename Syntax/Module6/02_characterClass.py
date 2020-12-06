import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")


find_match('[aeiouAEIOU]', "a", 1) # Y
find_match('[aeiouAEIOU]', "ab", 2) # Y
find_match('[aeiouAEIOU]', "b", 3) # N

find_match('[a-zA-Z0-9_]', "b", 4) # Y
find_match('[a-zA-Z0-9_]', ",", 5) # N
find_match('[a-zA-Z0-9_]', "-", 6) # N
find_match('[a-zA-Z0-9_-]', "-", 7) # Y (search '-')

#NOT
find_match('[^0-9]', "0", 8) # N
find_match('[^0-9]', "0a", 9) # Y

find_match('[aeiouAEIOU][a-zA-Z0-9_][^0-9]', "a", 10) # N
find_match('[aeiouAEIOU][a-zA-Z0-9_][^0-9]', "am?", 11) # Y
find_match('[aeiouAEIOU][a-zA-Z0-9_][^0-9]', "-aaa??", 12) # Y (because of the aaa)
find_match('[aeiouAEIOU][a-zA-Z0-9_][^0-9]', "-a?-a?-a?", 13) # N because of the ?- between

