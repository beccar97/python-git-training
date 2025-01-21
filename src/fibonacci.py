def compute_fibonacci_number(position: int | None) -> int | None:
    not_none_position = position
    if not_none_position is None:
        not_none_position = 1
    i = 1
    j = 1

    if not_none_position <= 2:
        return 1

    current_position = 2
    while current_position < not_none_position:
        temp = i
        i = j
        j += temp
        current_position += 1

    return j
