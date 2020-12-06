#slide 5
from findMatch import find_match

#\d - is the same as [0-9]
#\D - is the same as [^0-9]
find_match(r'\d$', '1', 1) # Y
find_match(r'\d$', 'a', 2) # N
find_match(r'\D$', '1', 3) # N
find_match(r'\D$', 'a', 4) # Y
