from typing import List


def compute_fibonacci_number(position: int) -> int:
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


def compute_fibonacci_list(start: int, end: int) -> List[int]:
    input_list = range(start, end + 1)
    return [compute_fibonacci_number(x) for x in input_list]
