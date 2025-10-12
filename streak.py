from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Returns the length of the longest run of consecutive positive numbers.

    Rules:
    - An empty list returns 0.
    - Zeros or negative numbers break the streak.
    - The function must be pure and deterministic (no randomness, prints, or global state).

    Examples:
    >>> longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4])
    3
    >>> longest_positive_streak([])
    0
    >>> longest_positive_streak([1, 1, 1])
    3
    """
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0

    max_streak = max(max_streak, current_streak)

    return max_streak