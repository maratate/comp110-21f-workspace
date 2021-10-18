"""Example of functions imported elsewhere."""

THE_ANSWER: int = 42 

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n

print(f"imports.py: {__name__}")