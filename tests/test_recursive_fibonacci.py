from src import compute_fibonacci_number


def test_recursive_fibonacci_works_for_small_numbers():
    expected_outputs = [1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i in range(0, len(expected_outputs)):
        assert compute_fibonacci_number(i + 1, True) == expected_outputs[i]
