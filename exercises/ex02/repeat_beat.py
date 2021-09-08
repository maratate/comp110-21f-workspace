"""Repeating a beat in a loop."""

__author__ = "7303804808"


# Begin your solution here...
beat: str = (input("What beat do you want to repeat?"))
number: int = int(input("How many times do you want to repeat it?"))
i: int = 0 

while i < 1:
    print(((beat + " ") * (number - 1) + beat))
    i = i + 1 
if number <= 0:
    print("No beat...")