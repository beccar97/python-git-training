from src import compute_fibonacci_number


def test_fibonacci_works_for_none_input():
    assert compute_fibonacci_number(None) == 1
