#slide 7
import re

#find first match of number and letter
line = 'my age is 22a years old'
m = re.search(r'(\d+).*', line)
if m:
    print(f"match string is {m.group(1)} in index ({m.start(1)},{m.end(1)})")
else:
    print("No match")