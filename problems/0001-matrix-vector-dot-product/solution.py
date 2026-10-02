def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    # Handle the edge case of an empty matrix
    if not a or not a[0]:
        if len(b) != 0:
            return -1
        else:
            return []

    # Get dimensions 
    rows = len(a)
    col = len(a[0])
    vec_len = len(b)
    result = []

    # Check condition and perform dot product
    if col == vec_len:
        for i in range(rows):
            row_sum = 0
            for j in range(col):
                row_sum += a[i][j] * b[j]
            result.append(row_sum)
        return result
    else:
        return -1
