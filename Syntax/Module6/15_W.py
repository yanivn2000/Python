#slide 5
from findMatch import find_match

#\w is the same as [a-zA-Z0-9_]
#\W is the same as [^a-zA-Z0-9_]
find_match(r'\w$', 'a', 1) # Y
find_match(r'\w$', '?', 2) # N

find_match(r'\W$', 'a', 3) # N
find_match(r'\W$', '?', 4) # Y
