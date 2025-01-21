def compute_fibonacci_number(position: int, is_recursive: bool = False) -> int:
    if is_recursive:
        return recursive_fibonacci(position)

    i = 1
    j = 1

    if position <= 2:
        return 1

    current_position = 2
    while current_position < position:
        temp = i
        i = j
        j += temp
        current_position += 1

    return j


def recursive_fibonacci(
    initial_position: int, left: int = 0, right: int = 1, position: int = None
) -> int:
    current_position = position if position is not None else initial_position

    if initial_position == 0:
        return 0
    if current_position == 0:
        return left
    if initial_position > 0:
        return recursive_fibonacci(
            initial_position, right, left + right, current_position - 1
        )
    else:
        return recursive_fibonacci(
            initial_position, right - left, left, current_position + 1
        )
