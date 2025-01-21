def compute_fibonacci_number(position: int) -> int:

    if position == 0:
        return 0
    if position < 0:
        return compute_negative_fibonacci_number(position)
    if position <= 2:
        return 1

    i = 1
    j = 1

    current_position = 2
    while current_position < position:
        temp = i
        i = j
        j += temp
        current_position += 1

    return j


def compute_negative_fibonacci_number(position: int) -> int:
    if position >= 0:
        raise Exception(f"Position must be less than zero! Received {position}.")

    resultIsNegative = position % 2 == 0
    absoluteResult = compute_fibonacci_number(-position)
    return -1 * absoluteResult if resultIsNegative else absoluteResult
