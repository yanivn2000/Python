#slide 6
import re

#find first match of number and letter
matchObj = re.search(r'\d[a-z]', 'bbb0a1c3d')

print(matchObj.group()) # 0a
print(matchObj.start()) # 3
print(matchObj.end()) # 5
