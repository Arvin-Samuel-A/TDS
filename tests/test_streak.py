import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test with a list containing only negative numbers and zeros."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_mixed_numbers_and_zero():
    """Test with a mix of positive, negative, and zero values."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks():
    """Test that the longest streak is correctly identified among multiple streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 1, 2, 3, 4, 5]) == 5

def test_streak_at_the_beginning():
    """Test a streak at the beginning of the list."""
    assert longest_positive_streak([5, 6, 7, -1, 2, 3]) == 3

def test_streak_at_the_end():
    """Test a streak at the end of the list."""
    assert longest_positive_streak([-1, 2, 0, 5, 6, 7]) == 3

def test_list_with_only_zeros():
    """Test a list containing only zeros."""
    assert longest_positive_streak([0, 0, 0, 0]) == 0

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_negative_number():
    """Test a list with a single negative number."""
    assert longest_positive_streak([-5]) == 0

def test_from_prompt_1():
    """Test first example from prompt."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_from_prompt_2():
    """Test second example from prompt."""
    assert longest_positive_streak([]) == 0

def test_from_prompt_3():
    """Test third example from prompt."""
    assert longest_positive_streak([1, 1, 1]) == 3