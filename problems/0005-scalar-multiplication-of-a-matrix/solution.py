def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	rows= len(matrix)
	cols =len(matrix[0])

	for i in range(rows):
		for j in range((cols)):
			matrix[j][i]*=scalar
	
	return matrix