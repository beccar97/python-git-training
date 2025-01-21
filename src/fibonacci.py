def compute_fibonacci_number(position: int, recursion: bool = False) -> int:
    if recursion:
        return recursive_fibonacci(1, 1, position - 2)

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


def recursive_fibonacci(previous: int, current: int, steps_left: int) -> int:
    if steps_left < 0:
        return 1

    match steps_left:
        case 0:
            return current
        case _:
            return recursive_fibonacci(current, previous + current, steps_left - 1)
