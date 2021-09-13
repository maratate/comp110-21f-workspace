"""Finding duplicate letters in a word."""

__author__ = "730384808"
word: str = input("Enter a word: ")
duplicate: bool = False 
i: int = 0 
j: int = i + 1

while i <= ((len(word)) - 1):
    while j <= ((len(word) - 1)):
        if word[i] == word[j]:
            duplicate = True 
        j = j + 1 
    i = i + 1 
if duplicate is True: 
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
