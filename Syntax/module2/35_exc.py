#insert the last element into position 3 in the list
#input is at least 4 words















str=input("Please insert a string:")
list=str.split()
list.insert(2,list.pop()) #add in position - do not overwrite
outputStr=' '.join(list)
print(outputStr)