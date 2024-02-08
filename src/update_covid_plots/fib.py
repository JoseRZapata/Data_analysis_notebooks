def fib(n: int) -> list[int]:
    """
    Python 3: Fibonacci series up to n

    Args:
        n (int): The upper limit of the Fibonacci series

    Returns:
        list[int]: The Fibonacci series up to n

    Example:
        >>> fib(1000)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    """
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
