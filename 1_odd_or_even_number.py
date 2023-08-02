# request a number for the user
num = int(input('Enter a number to know if it is even or odd: '))

# check if the number is even or odd
if num % 2 == 0:
    print(f'{num} is an even number!')
else:
    print(f'{num} is an odd number!')
