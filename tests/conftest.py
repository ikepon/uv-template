"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_numbers() -> list[int]:
    """Provide a sample list of numbers for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_float_numbers() -> list[float]:
    """Provide a sample list of float numbers for testing."""
    return [1.5, 2.5, 3.0, 4.5]


@pytest.fixture
def empty_list() -> list[int]:
    """Provide an empty list for testing."""
    return []


@pytest.fixture
def mixed_numbers() -> list[int | float]:
    """Provide a mixed list of integers and floats for testing."""
    return [1, 2.5, 3, 4.5, 5]


# Example of how to use fixtures in tests:
# def test_with_fixture(sample_numbers: list[int]) -> None:
#     result = calculate_sum(sample_numbers)
#     assert result == 15
