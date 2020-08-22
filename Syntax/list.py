numbers = [1,8,6,4,5]
print("append 22")
numbers.append(22)
print("insert(1,99)")
numbers.insert(1,99)
print(f"Pop: {numbers.pop()}")
numbers.remove(4)
print("removed 4")
numbers.insert(0,4)
print(f"insert 4")
print(numbers)
print(50 in numbers) #a way to check with OUT error of 50 is in the list
print(numbers.count(5))
numbers.sort()#return None (object)
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)#this array is a COPY - no change for the original array

#tuples - Immutable lists
print("tuples - Immutable lists")
numbers = (1,2,3)
#numbers[0] = 10 #WRONG!
print(numbers)
x = numbers[2]
print(x)

#unpacking (tubles and lists)
x,y,z = numbers
print(f"x {x}, y {y}, z {z}")

print("******** Spli a text ********")
words = "hey there! how are you?".split()
for word in words:
    print(word)