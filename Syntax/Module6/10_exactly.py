from findMatch import find_match

#optionl a-z. char, optional 0-9, end
find_match('^[a-z]{2}$', '', 1) # N
find_match('^[a-z]{2}$', 'a', 2) # N
find_match('^[a-z]{2}$', 'aa', 3) # Y
find_match('^[a-z]{2}$', 'aaa', 4) # N
