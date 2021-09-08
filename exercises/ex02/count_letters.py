"""Counting letters in a string."""

__author__ = "730384808"


# Begin your solution here...
letter: str = str(input("What letter do you want to look for?"))
word: str = str(input("Enter a word:"))
i: int = 0 
count: int = 0
while i < len(word):
    if (word[i]) == letter:
        count = count + 1 
    else:
        count == 0
    i = i + 1 
print("Count:" + str(count))