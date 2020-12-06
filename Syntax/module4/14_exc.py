#The functoin gets 2 parameters
#1. Char
#2. Words (unknown number)
#The function will print the number of words star with the char


def count(char, *words):
    res = 0
    for string in words:
        if string.startswith(char):
            res+=1
    print(res)

count("Y", "Yaniv", "Yada", "Hey", "Bye")
count("A", "Yaniv", "Yada", "Hey", "Bye")