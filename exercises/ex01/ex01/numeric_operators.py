"""Practicing with Numeric Operators."""
__author__ = 730384808
Left: str = input("What number?")
Right: str = input("What number?")
print("Left-hand side: " + Left)
print("Right-hand side: " + Right)
answer: str = int(Left)**int(Right)
print(str(Left) + str(" ** ") + str(Right) + " is " + str(answer))
answer_2: float = float(Left) / float(Right)
print(str(Left) + str(" / ") + str(Right) + (" is ") + str(answer_2))
answer_3: int = int(Left) // int(Right)
print(str(Left) + str(" // ") + str(Right) + (" is ") + str(answer_3))
answer_4: int = int(Left) % int(Right)
print(str(Left) + str(" % ") + str(Right) + (" is ") + str(answer_4))