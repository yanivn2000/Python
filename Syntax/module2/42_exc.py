#count the number of characters per word
#for example: My name is Yaniv
#will print
#My-2 name-4 is-2 Yaniv-5

inputString=input("Insert a string: ")
list = inputString.split()
list2 = [s+ '-'+str(len(s)) for s in list]
res = ' '.join(list2)
print(res)