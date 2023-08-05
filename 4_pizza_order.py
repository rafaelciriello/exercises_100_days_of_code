"""Asks the user to choose the size of a pizza, 
whether or not to add pepperoni and cheese, 
and returns the total value"""

# ask the user to choose size, pepperoni and cheese
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

bill = 0

# check size and add amount to bill
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("The selected pizza size does not exist!")

# check if added pepperoni 
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# check if added cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
