#input a number
#for example: 11116665244433
#The output will be the unique digits
# 123456


inputStr=input("Please enter a number: ")
allDifits = [x for x in inputStr]
uniquDigits = set(allDifits) #[1,1,1,2,2,2] => {1,2}
res = ''.join(uniquDigits)
print(res)

#Extra
#print(''.join(set(inputStr)))
