from src.update_covid_plots.fib import fib


def test_fib() -> None:
    """
    Tests the function fib.
    This function asserts that the function fib returns the
    correct Fibonacci series up to a given number.
    The Fibonacci series is tested for the numbers 5, 10, and 15.

    Raises:
        AssertionError: If any of the assertions fail, an AssertionError is raised.
    """
    assert fib(5) == [0, 1, 1, 2, 3]
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fib(15) == [0, 1, 1, 2, 3, 5, 8, 13]
