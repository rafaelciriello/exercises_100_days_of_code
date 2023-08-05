"""Asks the user for two names, concatenates them into a single string, 
checks the occurrence of the letters (t r u e l o v e) and returns a 
two-digit number as the love index"""

# Love Calculator
print("Welcome to the Love Calculator!")

# request to user names
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# combine the names into a single string
combined_string = name1 + name2

# count the incidence of the letters of the word true in the string
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

# count the incidence of the letters of the word love in the string
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")

# calculate the love score based on the occurrence of letters within the string
true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))

# check the love score interval and give feedback to the user
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}!")
