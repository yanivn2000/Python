#slide 7
import re


def find_digit(num):
    txt = str(num)
    m = re.search(r'^[\d]+\.(\d)[\d]*$', txt)
    if m:
        print(m.group(1))
    else:
        print(("No match"))

find_digit(1234.5678) # 5
find_digit(12.74) # 7
find_digit(24) # No Match
