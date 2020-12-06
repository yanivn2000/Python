#slide 7
import re

#find first match of number and letter
txt = 'b0a1c3d'
matchObj = re.search(r'(\d)a1([a-z])', txt)
print(txt[matchObj.start():matchObj.end()])
print(matchObj.start())
print(matchObj.end())