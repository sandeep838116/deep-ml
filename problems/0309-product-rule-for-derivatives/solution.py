import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    # Multiply the polynomials
    product = np.convolve(f_coeffs,g_coeffs)
     # Differentiate
    result = [i * product[i] for i in range(1, len(product))]

    # Round
    result = [round(float(x), 4) for x in result]

    # Remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result if result else [0.0]