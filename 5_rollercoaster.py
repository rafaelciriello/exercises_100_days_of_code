"""Asks the user for height, authorizes or not the sale of the ticket, 
calculates the value considering age and added a photo 
and returns the total value of the ticket"""

# rollercoaster
print("Welcome to the rollercoaster!")

height = int(input("What's your height in cm?\n"))
bill = 0

# check minimum height
if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What's your age? "))

    # check ticket value
    if age < 12:
        print("Child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    elif age >= 45 and age <= 55:
        print("Your tickets are $0")
    else:
        print("Adult tickets are $12.")
        bill += 12

    # check if there is a request for a photo
    wants_photo = input("Do you have a photo? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3

else:
    print("Sorry, you can't ride the rollercoaster!")

print(f'The total of your ticket is ${bill}')
