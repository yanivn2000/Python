
def welcome_message(first_name, last_name):
    print(f"Welcome {first_name} {last_name} to our software")
    print("Let's get started")

print("Start")
fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
welcome_message(fname,lname)
#welcome_message(first_name=fname,last_name=lname)#position arguments
#welcome_message(last_name=lname, first_name=fname)
print("Finished")
#we need 2 blank lines after a function


