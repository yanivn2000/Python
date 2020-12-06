#slide 7
import re

#find first match of number and letter
line = '27:11:2004'
m = re.search(r'(\d+):(\d+):(\d+)*', line)
if m:
    print(f"match day is {m.group(1)} in index ({m.start(1)},{m.end(1)})")
    print(f"match month is {m.group(2)} in index ({m.start(2)},{m.end(2)})")
    print(f"match year is {m.group(3)} in index ({m.start(3)},{m.end(3)})")
else:
    print("No match")