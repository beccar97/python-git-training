from src import compute_fibonacci_list


def test_fibonacci_list_works_for_small_range():
    start_number = 3
    end_number = 11
    expected_outputs = [2, 3, 5, 8, 13, 21, 34, 55, 89]

    assert compute_fibonacci_list(start_number, end_number) == expected_outputs
