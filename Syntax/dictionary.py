#key value pairs
print("******** Simple dictionary ********")
customer = {
    "name" : "Yaniv Nuriel",
    "age" : 43,
    "isIsraeli" : True
}

print(customer["name"])
#print(customer["birthday"])#this is crush
print(customer.get("AGE"))
print(customer.get("age"))

customer["age"] = 44
print(customer.get("age"))

#Convert numbers to words
print("******** Convert numbers to words ********")
convert_numbers = {
    "1": "Ome",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

phone = input("Enter a phone: ")
for digit in phone:
    print(convert_numbers[digit])


print("******** Convert sad to happy and bad to good ********")
def bad_words_convertor(message):
    words = message.split()
    hebrew = {
        "sad" : "happy",
        "bad" : "good"
    }
    output=""
    for word in words:
        output += hebrew.get(word,word) + " " #return the word if doesn't find!

    return output

message=input(">")
print(bad_words_convertor(message))