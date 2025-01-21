def compute_fibonacci_number(position: int) -> int:

    if position == 1 or position == 2:
        return 1

    small_fibonacci_number = 1
    large_fibonacci_number = 1

    current_position = 2
    while current_position < position:
        next_fibonacci_number = small_fibonacci_number + large_fibonacci_number
        small_fibonacci_number = large_fibonacci_number
        large_fibonacci_number = next_fibonacci_number

        current_position += 1

    return large_fibonacci_number
