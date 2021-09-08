"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730384808"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
number: int = randint(1, 4)
if number == 1:
    print("A great person will come into your life.")
else:
    if number == 2:
        print("You will have a great year.")
    else:
        if number == 3:
            print("A fresh start will put you on your way.")
        else:
            if number == 4:
                print("Good things come to people who are patient.")
print("Now, go spread positive vibes!")