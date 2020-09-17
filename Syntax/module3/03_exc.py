#Read from the user a name of a Month
#e.g. Feb
#The program will print the number of days in that month
#In case the user insert a wrong month the program will print an error information


month=input("Please insert a name of a month: ")
if month in ("January", "March", "May", "July", "August", "October", "December"):
        print("31 days")
elif month in ("April", "June", "September", "November"):
        print("30 days")
elif(month == "February"):
        print("28 or 29 days")
else:
    print("Wrong input!")


