"""Tests for example_package.main module."""

import pytest

from example_package.main import calculate_sum, greeting, is_even


class TestGreeting:
    """Tests for the greeting function."""

    def test_greeting_basic(self) -> None:
        """Test basic greeting functionality."""
        result = greeting("World")
        assert result == "Hello, World!"

    def test_greeting_with_japanese(self) -> None:
        """Test greeting with Japanese characters."""
        result = greeting("世界")
        assert result == "Hello, 世界!"

    def test_greeting_with_whitespace(self) -> None:
        """Test greeting strips whitespace from name."""
        result = greeting("  Python  ")
        assert result == "Hello, Python!"

    def test_greeting_empty_string_raises_error(self) -> None:
        """Test greeting raises ValueError for empty string."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greeting("")

    def test_greeting_whitespace_only_raises_error(self) -> None:
        """Test greeting raises ValueError for whitespace-only string."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greeting("   ")

    @pytest.mark.parametrize("name,expected", [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("123", "Hello, 123!"),
        ("special@chars", "Hello, special@chars!"),
    ])
    def test_greeting_parametrized(self, name: str, expected: str) -> None:
        """Test greeting with various names."""
        result = greeting(name)
        assert result == expected


class TestCalculateSum:
    """Tests for the calculate_sum function."""

    def test_calculate_sum_integers(self) -> None:
        """Test sum calculation with integers."""
        result = calculate_sum([1, 2, 3, 4, 5])
        assert result == 15

    def test_calculate_sum_floats(self) -> None:
        """Test sum calculation with floats."""
        result = calculate_sum([1.5, 2.5, 3.0])
        assert result == 7.0

    def test_calculate_sum_mixed_numbers(self) -> None:
        """Test sum calculation with mixed int and float."""
        result = calculate_sum([1, 2.5, 3])
        assert result == 6.5

    def test_calculate_sum_single_number(self) -> None:
        """Test sum calculation with single number."""
        result = calculate_sum([42])
        assert result == 42

    def test_calculate_sum_negative_numbers(self) -> None:
        """Test sum calculation with negative numbers."""
        result = calculate_sum([-1, -2, -3])
        assert result == -6

    def test_calculate_sum_zero_sum(self) -> None:
        """Test sum calculation that results in zero."""
        result = calculate_sum([-5, 5])
        assert result == 0

    def test_calculate_sum_empty_list_raises_error(self) -> None:
        """Test calculate_sum raises ValueError for empty list."""
        with pytest.raises(ValueError, match="Cannot calculate sum of empty list"):
            calculate_sum([])

    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 3], 6),
        ([10, -5, 0], 5),
        ([0.1, 0.2, 0.3], pytest.approx(0.6)),
        ([100], 100),
        ([-1, 1, -1, 1], 0),
    ])
    def test_calculate_sum_parametrized(self, numbers: list[int | float], expected: int | float) -> None:
        """Test sum calculation with various number combinations."""
        result = calculate_sum(numbers)
        assert result == expected


class TestIsEven:
    """Tests for the is_even function."""

    def test_is_even_positive_even(self) -> None:
        """Test is_even with positive even numbers."""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True

    def test_is_even_positive_odd(self) -> None:
        """Test is_even with positive odd numbers."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_is_even_zero(self) -> None:
        """Test is_even with zero."""
        assert is_even(0) is True

    def test_is_even_negative_even(self) -> None:
        """Test is_even with negative even numbers."""
        assert is_even(-2) is True
        assert is_even(-4) is True
        assert is_even(-100) is True

    def test_is_even_negative_odd(self) -> None:
        """Test is_even with negative odd numbers."""
        assert is_even(-1) is False
        assert is_even(-3) is False
        assert is_even(-99) is False

    @pytest.mark.parametrize("number,expected", [
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (-1, False),
        (-2, True),
        (1000, True),
        (1001, False),
    ])
    def test_is_even_parametrized(self, number: int, expected: bool) -> None:
        """Test is_even with various numbers."""
        result = is_even(number)
        assert result is expected