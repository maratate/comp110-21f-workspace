
"""Guess That Number Game."""
__author__ = "730384808"

from random import randint

points: int = 0
player: str = ""
CELEBRATION_EMOJI: str = '\U0001F973'
SAD_EMOJI: str = '\U0001F622'


def main() -> None:
    """The program's entrypoint."""
    greet()
    global points
    points = 0 
    player_choice: int = int(input(f"{player}, choose your adventure! 1: Guess the number 1-5. 2: Guess the number 1-10. 3: Leave the game. Choose an option 1-3: "))
    while points >= 0: 
        if player_choice == 1:
            number_1: int = int(input("Guess the number 1-5: "))
            game1(number_1)
            print(f"You have {points} adventure point(s).")
        if player_choice == 2: 
            number_2: int = int(input("Guess the number 1-10: "))
            print(f"You have {game_2(number_2)} adventure point(s)!")
        if player_choice == 3:
            print(f"Game over {player}, goodbye {SAD_EMOJI}! You had {points} adventure point(s).")
            points = points - 1 
            quit()
        player_choice: int = int(input(f"{player}, choose your adventure! 1: Guess the number 1-5. 2: Guess the number 1-10. 3: Leave the game. Choose an option 1-3: "))


def greet() -> None:  
    """Greeting."""
    global player
    player = input("What is your player name? ")
    print(f"{player}, welcome to the Guess That Number Game! Try to guess the number and everytime you guess correctly you will recieve 1 adventure point.")


def game1(x: int) -> None: 
    """Game 1! Guess the number 1-5."""
    global player
    global points
    number = randint(1, 5)
    if x == number: 
        points = points + 1
        print(f"You win {CELEBRATION_EMOJI}! You have {points} adventure points.")
    else: 
        print(f"That was incorrect {SAD_EMOJI}. Try again!") 
            

def game_2(x: int) -> int: 
    """Game 2! Guess the number 1-10."""
    global points
    guess_2 = randint(1, 10)
    if guess_2 == x:
        print(f"You guessed correctly {CELEBRATION_EMOJI}!")
        points = points + 1 
    else: 
        print(f"That was incorrect {SAD_EMOJI}. Try again!")
    return(int(points))


if __name__ == "__main__":
    main()