def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    if not vectors or not vectors[0]:
        return []
        
    num_vars = len(vectors)
    n = len(vectors[0])
    
    # Protect against ZeroDivisionError (n - 1)
    if n < 2:
        raise ValueError("At least 2 observations are required to calculate sample covariance.")

    # Calculate the mean
    means = [sum(vector) / n for vector in vectors]

    # Initialize an N x N matrix with zeros
    cov_matrix = [[0.0] * num_vars for _ in range(num_vars)]
    
    for i in range(num_vars):
        for j in range(i, num_vars):
            mean_i = means[i]
            mean_j = means[j]

            cov_ij = sum((vectors[i][k] - mean_i) * (vectors[j][k] - mean_j) for k in range(n)) / (n - 1)
            
            cov_matrix[i][j] = cov_ij
            cov_matrix[j][i] = cov_ij

    return cov_matrix