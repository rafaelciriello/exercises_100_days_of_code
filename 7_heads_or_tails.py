'''Create a Heads or Tails game using random module and conditional statements if and else'''

# Import random modulo
import random

# Randomize two integers and assign the values "head" or "tail" to coin
coin = random.randint(1, 2)
if coin == 1:
    print("Tails")
else:
    print("Heads")
    