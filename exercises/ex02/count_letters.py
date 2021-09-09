"""Counting letters in a string."""

__author__ = "730384808"


# Begin your solution here...
letter: str = input("What letter do you want to look for?")
word: str = input("Enter a word:")
letter_count = int = 0 
i = int = 0 
while i < len(word):
    if (word[i]) == letter:
        letter_count = (letter_count) + 1 
    i = i + 1 
print("Count: " + str(letter_count))