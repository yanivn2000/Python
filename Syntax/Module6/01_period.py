import re

txt = "Yaniv Nuriel"

#do we have 1 character that is not a new line in th text?
x = re.search(".", txt)

if x:
    print("1 - Match" )#<- this is printed
else:
    print("1 - No Match")

#do we have 20 characters that are not a new line in th text?
x = re.search("....................", txt)

if x:
    print("2 - Match")
else:
    print("2 - No Match") #<- this is printed


#the index is mapping to the test that we are running
def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")


find_match(".", txt, 3)
find_match("....................", txt, 4)