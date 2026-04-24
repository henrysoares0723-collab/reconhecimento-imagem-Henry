def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    A prime number is greater than 1 with no positive divisors other than 1 and itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True