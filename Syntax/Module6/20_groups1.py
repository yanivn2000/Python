#slide 6
import re

#find first match of number and letter
matchObj = re.search(r'\d[a-z]', 'bb0a1c3d')

print(matchObj.group()) # 0a
print(matchObj.start()) # 2
print(matchObj.end()) # 4
print(matchObj.groups()) # () returns empty group

#group the number and group the letter
matchObj = re.search(r'(\d)a([a-z])', 'bb0ab1c3d')

print(matchObj.group()) # 0ab
print(matchObj.start()) # 2
print(matchObj.end()) # 5
print(matchObj.groups()) # ('0', 'b')

print(matchObj.group(1)) # 0
print(matchObj.start(1)) # 2
print(matchObj.end(1)) # 3
print(matchObj.group(2)) # b
print(matchObj.start(2)) # 4
print(matchObj.end(2)) # 5

