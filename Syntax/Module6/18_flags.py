#slide 6
import re

matchObj = re.search('A', 'b0a1')

if matchObj is not None:
    print("Match")
else:
    print("No Match") # <- This

matchObj = re.search('A', 'b0a1', re.IGNORECASE)

if matchObj is not None:
    print("Match") # <- This
else:
    print("No Match")