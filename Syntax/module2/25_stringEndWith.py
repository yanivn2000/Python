str="Python programming is easyo learn"

#start parameter is 7
result=str.endswith("learn",7) #True
print(result)

result=str.endswith("is",7, 20) #False
print(result)

result=str.endswith("easy",7,26) #True
print(result)