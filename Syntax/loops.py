#Guess a number
print("******* Guess a number game *******")
screret_number=9
number_of_guess = 0
guess_limit = 3

while number_of_guess < guess_limit:
    if(int(input(">")) == screret_number):
        print("You guessed it!")
        break
    else:
        number_of_guess += 1
if(number_of_guess == guess_limit):
    print("You failed")
    

#State machin
print("******* Car immulator *******")
command=""
car_started = False
while command.lower() != "quit":
    command = input("> ").lower()
    if(command == "start"):
        if car_started:
            print("Car is already started.")
        else:
            car_started = True
            print("Car is started...")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped")
        else:
            car_started = False
            print("Car has stopped.")
    elif command == "help":
        print("""
        start = to start the car
        stop - to stop the car
        help - to see menu
        """)
    elif command == "quit":
        break

#for in
print("******* For in *******")
for item in 'Python':
    print(item)

for item in ["bmw", "opel", "Jaguar"]:
    print(item)

#range function create an object for each iteratoin
for item in range(10):
    print(item)
for item in range(5, 10):
    print(item)   
for item in range(5, 10, 2):
    print(item)    


#nested loop
for x in range(4):
    for y in range(10):
        print(f"{x}, {y}")

#draw F
#one option
print("x" * 5)
#second option
numbers = [5,2,5,2,2]
for item in numbers:
    output = ""
    for x in range(item):
        output += "X"
    print(output)