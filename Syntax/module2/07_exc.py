#Write a program that reads 3 values from the user
#Check if value1 + value2 equal number3
#put the result in boolean value



val1=int(input("Please enter first number:"))
val2=int(input("Please enter second number:"))
val3=int(input("Please enter third number:"))

#OR
# val1=int(input("Please enter first number:"))
# val2=int(input("Please enter second number:"))
# val3=int(input("Please enter third number:"))
# val1=int(val1)
# val2=int(val2)
# val3=int(val3)

isEq = val1 + val2 == val3
print(isEq)

#OR
# if(val1+val2 == val3):
#     print(f"{val1} + {val2} = {val3}")
# else:
#     print(f"{val1} + {val2} != {val3}")
