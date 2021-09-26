"""Example of a function that processes a list."""


def main() -> None:
    names: list[str] = ["Kris", "Kaki", "Kris"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool: 
    """Return True if needle is found in the haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True 
        i += 1 
    return False 