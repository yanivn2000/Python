with open("input1.txt", "r") as fileObject:
    lineContent = fileObject.readline()
    while lineContent:
        print(lineContent)
        lineContent = fileObject.readline()

#first line (\n of the line)
#(\n of the print)
#second line (\n of the line)
#(\n of the print)
#third line (\n of the line)