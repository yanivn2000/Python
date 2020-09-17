#get string and print the number of each word



inputString=input("Please insert a string: ")
myDict = {}

for word in inputString.split():
    myDict[word] = myDict.get(word,0) + 1

for k , v in myDict.items():
    print(f"The number of occurances of word {k} is {v}")