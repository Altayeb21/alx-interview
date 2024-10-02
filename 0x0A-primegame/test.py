#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

def run_tests():
    test_cases = [
        # Valid cases
        (5, [2, 5, 1, 4, 3], 'Ben'),
        (3, [4, 5, 1], 'Ben'),
        (4, [10, 20, 30, 40], 'Ben'),
        (2, [2, 3], None),  # Ben should win both
        (1, [11], 'Maria'),  # Maria wins on 11

        # Edge cases
        (0, [], None),  # No rounds
        (1, [1], 'Ben'),  # 1 is not a prime number
        (3, [1, 1, 1], 'Ben'),  # All rounds are invalid
        
        # Invalid inputs
        ('five', [2, 3, 5], None),  # x is not an integer
        (3, 'not a list', None),  # nums is not a list
        (-1, [2, 3, 5], None),  # x is negative
    ]

    for i, (x, nums, expected) in enumerate(test_cases):
        result = isWinner(x, nums)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: {result}")

if __name__ == "__main__":
    run_tests()
