from findMatch import find_match

#at least 2 characters
find_match('^[a-z]{2,}$', '', 1) # N
find_match('^[a-z]{2,}$', 'a', 1) # N
find_match('^[a-z]{2,}$', 'aa', 1) # Y
find_match('^[a-z]{2,}$', 'aaa', 1) # Y
