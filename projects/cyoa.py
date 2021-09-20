
"""Guess That Number Game."""
__author__ = "730384808"

from random import randint

points: int = 0
player: str = ""


def main() -> None:
    """The program's entrypoint."""
    greet()
    global points
    points = 0 
    player_choice: int = int(input("Choose your adventure! 1: Guess the number 1-10. 2: Guess the number 1-50. 3: Leave the game. Choose an option?"))
    while points >= 0: 
        if player_choice == 1:
            number: str = input("Choose a number 1-10.")
            game1(number)
        if player_choice == 2: 
            number_2: str = input("Choose a number 1-50.")
            game_2(number_2)
        if player_choice == 3:
            print(f"Game over {player}, goodbye! You had {points} adventure points.")


def greet() -> None:  
    """Greeting."""
    global player
    player = input("What is your player name? ")
    print(f"{player}, welcome to the Guess That Number Game! Try to guess the number in as few guesses as possible. Everytime you guess you will recieve 1 adventure point.")


def game1() -> None: 
    """Game 1! Guess the number 1-10."""
    global player
    global points
    number: int = randint(1, 10)
    while points < 10: 
        guess: str = (input(f"{player}, guess the number between 1 and 10."))
        if guess == number: 
            print(f"(You win! You got {points} adventure points.")
        else: 
            print(" That was incorrect. Guess again")
            points = points + 1 
            

def game_2(number_2) -> int: 
    """Game 2! Guess the number 1-50."""
    global points
    number_2: int = randint(1, 30)
    while points < 30: 
        guess_2: str = (input("Guess the number between 1 and 10."))
        if guess_2 == number_2:
            print(f"(You win! You got {points} adventure points.")
        else: 
            print("That was incorrect. Guess again.")
            points = points + 1 
            return(points)


if __name__ == "__main__":
    main()