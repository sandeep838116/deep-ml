def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	# Get dimension
	rows = len(matrix)
	cols = len(matrix[0])

	result =[]

	# Calculate mean 
	if (mode =='column'):
		for i in range(cols):
			sum =0
			for j in range (rows):
				sum += matrix[j][i]
			means = sum/rows
			result.append(means)
	else:
		for j in range(rows):
			sum =0
			for i in range(cols):
				sum+=matrix[j][i]
			means = sum/cols
			result.append(means)

	return result