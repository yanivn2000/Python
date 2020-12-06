import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")

find_match('a', '0a', 1) # Y
find_match('^a', '0a', 2) # N
find_match('a', 'a0', 3) # Y
find_match('^a', 'a0', 4) # Y

find_match('a$', '0a', 5) # Y
find_match('a$', 'a0', 6) # N

find_match('^a$', 'a', 7) # Y
find_match('^a$', '0a', 8) # N
find_match('^a$', 'a0', 9) # N

#insdie the brackets the ^ is NOT
find_match('[^a]', 'a', 10) # N
find_match('[^a]', 'a0', 11) # Y
#starts at a
find_match('^[a]', 'a', 12) # Y
find_match('^[a]', 'a0', 13) # Y
