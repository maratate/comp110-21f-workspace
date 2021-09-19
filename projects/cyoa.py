"""Guess The Number Game."""
from random import randint
__author__ = "730384808"
points: int = 0 


def main() -> None:
    """The program's entrypoint"""
    greet()
print(input("Choose your adventure! Option 1: Guess the number 1-10. Option 2: Guess the number 1-50. Option 3: Leave the game. What would you like to do?")
    if input == 1 
        game1()
    if input == 2 
            game2(points)
    else: 
        print(f"Game over, goodbye! You had {points} adventure points.")


def greet() -> None  
    """Greeting."""
    player: str = input("What is your player name? ")
    print("player, welcome to the Guess That Number Game! Try to guess the number in as least guesses as possible. Everytime you guess you will recieve 1 adventure point.")
    return()

def game1() -> None: 
    """Game 1! Guess the number 1-10"""
    number: = randint(1 , 10)
    while points < 10
    print(input("Guess the number between 1 and 10."))
        if input == number 
            print(f"(You win! You got {points} adventure points.")
        else: 
            print(" That was incorrect. Guess again"
             points = points + 1 


def game2(x:int) -> int: 
    """Game 2! Guess the number 1-50"""
    number: = randint(1 , 50)
    while points < 50
    print(input("Guess the number between 1 and 10."))
        if input == number 
            print(f"(You win! You got {points} adventure points.")
        else: 
            print(" That was incorrect. Guess again"
            points = points + 1 

print(greet)
if __name__ == "__main__":
    main()