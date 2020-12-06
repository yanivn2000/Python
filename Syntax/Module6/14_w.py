#slide 5
from findMatch import find_match

#\w is the same as [a-zA-Z0-9_]
find_match(r'\w{5}$', 'a1A_v', 1) # Y
find_match(r'\w{5}$', 'a1A?v', 2) # N
find_match(r'\w{5}$', 'a1A_', 3) # N
