def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    rows =len(a)
    cols =len(a[0])

    transposed = []
    for col in range(cols):               
        new_row = []
        for row in range(rows):           
            new_row.append(a[row][col])
        transposed.append(new_row)
    return  transposed
    