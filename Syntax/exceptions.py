
print("******* Value error *******")
while True:
    try:
        age = int(input("Age: "))#may crush if user will enter a non number value
        break
    except ValueError: #in case the user will enter a value error
        print("Invalid age")

print(age)

#Devision byzero
print("******* Division by zero *******")
while True:
    try:
        number = int(input("number: "))#may crush if user will enter a non number value
        result = 1000/number
        break
    except ValueError: #in case the user will enter a value error
        print("Invalid age")
    except ZeroDivisionError: #in case the user will enter a value error
        print("number can not be zero")

print(result)