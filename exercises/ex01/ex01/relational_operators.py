"""Practicing with Relational Operators."""
__author__ = 730384808
Left: str = input("Choose a number.")
Right: str = input("Choose a number.")
print("Left-hand side: " + Left)
print("Right-hand side: " + Right)
answer: bool = (Left < Right)
print(str(Left) + str(" < ") + str(Right) + (" is ") + str(answer))
answer_2: bool = (Left >= Right)
print(str(Left) + str(" >= ") + str(Right) + (" is ") + str(answer_2))
answer_3: bool = (Left == Right)
print(str(Left) + str(" == ") + str(Right) + (" is ") + str(answer_3))
answer_4: bool = (Left != Right)
print(str(Left) + str(" != ") + str(Right) + (" is ") + str(answer_4))