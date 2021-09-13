"""Drawing forests in a loop."""

__author__ = "730384808"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
Depth: int = int(input("Depth: "))
i: int = 0
j: int = 0

while i < int(Depth):
    while j < Depth: 
        print(TREE * (Depth - (Depth - (i + 1))))
        i = i + 1 
        j = j + 1  