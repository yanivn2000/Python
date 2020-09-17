#action s on lists

#write a program that gets an odd numbers of items into list
#[1,2,3,4,5]
#identify the middle,
#swap the end with the start
#duplicate the middle 5 times
#[4,5,3,3,3,3,3,1,2]


str=input("Please insert a string (odd):")
list=str.split()
middle=len(list) // 2
part1=list[middle+1:]
part2=[list[middle]]*5 #list and not string
part3=list[:middle]

outputList=part1+part2+part3
outputStr = ' '.join(outputList)
print(outputStr)