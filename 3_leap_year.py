"""Aks the user to enter a year and returns whether or not it is a leap year"""

# ask the user for the year
year = int(input('Enter the year to find out if is a leap year: '))

# check whether or not it is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')
