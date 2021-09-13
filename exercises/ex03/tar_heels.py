"""An exercise in remainders and boolean logic."""

__author__ = "730384808"


# Begin your solution here...
integer: str = input("Enter an int: ")
if int(integer) % 2 == 0 and int(integer) % 7 == 0:
    print("TAR HEELS")
else:
    if int(integer) % 2 == 0:
        print("TAR")
    else:
        if int(integer) % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
