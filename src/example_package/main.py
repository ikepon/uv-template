"""Main module with example functions.

This module contains sample functions to demonstrate testing,
type hints, and documentation.
"""


def greeting(name: str) -> str:
    """Generate a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A formatted greeting string.

    Examples:
        >>> greeting("World")
        'Hello, World!'
        >>> greeting("Python")
        'Hello, Python!'
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    
    return f"Hello, {name.strip()}!"


def calculate_sum(numbers: list[int | float]) -> int | float:
    """Calculate the sum of a list of numbers.

    Args:
        numbers: List of numbers to sum.

    Returns:
        The sum of all numbers.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> calculate_sum([1, 2, 3])
        6
        >>> calculate_sum([1.5, 2.5])
        4.0
        >>> calculate_sum([])
        Traceback (most recent call last):
        ...
        ValueError: Cannot calculate sum of empty list
    """
    if not numbers:
        raise ValueError("Cannot calculate sum of empty list")
    
    return sum(numbers)


def is_even(number: int) -> bool:
    """Check if a number is even.

    Args:
        number: The number to check.

    Returns:
        True if the number is even, False otherwise.

    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
        >>> is_even(0)
        True
    """
    return number % 2 == 0