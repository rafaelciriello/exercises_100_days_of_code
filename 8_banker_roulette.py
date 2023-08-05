"""Asks the user for names and randomly selects one to pay the bill"""

# import random module
import random

# ask the user to enter the names
names_str = input("Give me everbody's names, separeted by a comma: ")

# separate the names in the string and add in a list "names"
names = names_str.split(', ')

# randomly select one of the names from the list and give feedback to the user
pay_the_bill = random.randint(0, len(names) -1)
print(f'{names[pay_the_bill]} will pay the bill today.')
