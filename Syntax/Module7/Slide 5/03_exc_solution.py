import re

with open("input2.txt", "r") as readObject:
    with open('output.txt', "w") as writeObject:
        lineContent = readObject.readline()
        lineIndex = 1
        while lineContent: # as long as we read line
            if lineIndex %2 == 1:
                line = re.sub('\n', ' ', lineContent)
                writeObject.write(line)
            lineContent = readObject.readline()
            lineIndex += 1
