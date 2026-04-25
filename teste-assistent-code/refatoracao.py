from typing import List, Tuple

def calculate_statistics(numbers: List[int]) -> Tuple[int, float, int, int]:
    """
    Calculate the total, mean, maximum, and minimum values of a list of numbers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, float, int, int]: A tuple containing total, mean, maximum, and minimum.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    total = sum(numbers)
    mean = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, mean, maximum, minimum

# Example usage
sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, mean, maximum, minimum = calculate_statistics(sample_numbers)

print("Total:", total)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)