#get string an print the number of each character

inputString=input("Please insert a string: ")
myDict = {}

for letter in inputString:
    myDict[letter] = myDict.get(letter,0) + 1

print(myDict)