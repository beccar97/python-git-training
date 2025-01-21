from src import compute_fibonacci_number


def test_negative_fibonacci_works_for_small_negative_numbers():
    inputs = [-6, -5, -4, -3, -2, -1]
    expected_outputs = [-8, 5, -3, 2, -1, 1]

    for i in range(0, len(expected_outputs)):
        assert compute_fibonacci_number(inputs[i]) == expected_outputs[i]
