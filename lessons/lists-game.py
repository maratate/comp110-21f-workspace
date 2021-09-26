"""Examples of using Lists in a simple "game'."""

from random import randint 

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1: 
    rolls.append(randint(1, 6))

print(rolls)

# remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of our rolls 
i: int = 0 
sum: int = 0 
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1 
print(f"Total score:{sum}")

# rolls: list[int] = list() 
# # sets up empty list 
# rolls.append(randint(1, 6)) 
# # method call 
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item 
# print(rolls[0])
# print(rolls[1])

# #Access the length of a list (number of items)
# print(len(rolls))

# #Access the last item in a list 
# last_index: int = len(rolls) - 1 
# print(rolls[last_index])