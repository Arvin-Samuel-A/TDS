import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6, 0, 1]) == 3
    assert longest_positive_streak([1, 2, 3, -1, 4, 5, 0, 1]) == 3

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4, 5, 6]) == 4

def test_streak_at_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 6]) == 4

def test_example_from_prompt():
    """Test the main example from the prompt."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3