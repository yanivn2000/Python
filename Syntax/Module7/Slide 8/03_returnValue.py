with open("output3.txt", 'w') as fileObject:
    numWritten = fileObject.write("Yaniv\n")
    print(numWritten) # 6 (including the \n)
    numWritten = fileObject.write("Nuriel, Tel Aviv")
    print(numWritten) # 16
