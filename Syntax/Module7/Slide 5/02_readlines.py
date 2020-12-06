with open("input1.txt", "r") as fileObject:
    lines = fileObject.readlines()
    print(lines) #['first line\n', 'second line\n', 'third line']

for line in lines:
    print(line)

# first line
#
# second line
#
# third line