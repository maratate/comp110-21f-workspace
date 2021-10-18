"""Practice with dictionaries."""

__author__ = "730384808"

# Define your functions below


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    new_dict = {}
    for x in dictionary: 
        if dictionary[x] not in new_dict:
            key = dictionary[x]
            new_dict[key] = x
        else:
            raise KeyError("KeyError: duplicate keys")
    return new_dict  


print(invert({"a": "x", "b": "y", "c": "z"}))

dictionary: dict[str, str] = {"mara": "red", "anna": "purple", "austin": "purple", "abby": "green"}


def favorite_color(names_and_colors: dict[str, str]) -> str: 
    """Returns color that appears most frquently in the dictionary."""
    color_count: dict[str, int] = {}
    color: str = "" 
    i: int = 0 
    for name in names_and_colors:
        color = names_and_colors[name]
        if color in color_count:
            color_count[color] += 1 
        else:
            color_count[color] = 1 
    for key in color_count:
        if color_count[key] > i:
            i = color_count[key] 
            color = key 
    return color 


print(favorite_color(dictionary))

practice_list: list[str] = ["mara", "elizabeth", "daly", "Katie", "daly", "daly", "Katie"]


def count(intial_list: list[str]) -> dict[str, int]:
    """Returns dictionary with keys and their count."""
    i: int = 0 
    result_dictionary: dict[str, int] = {}
    while len(intial_list) > i:
        if intial_list[i] not in result_dictionary:
            result_dictionary[(intial_list[i])] = 1 
        else: 
            result_dictionary[intial_list[i]] += 1
        i += 1 
    return result_dictionary


print(count(practice_list))