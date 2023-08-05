"""Asks for the user's weight and height and calculates their BMI"""

# request user height and weight
height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kg: '))

# calculate the bmi
bmi = round(weight / height ** 2)

# check the bmi and give feedback
if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinicaly obese.')
