import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g=0
    h=0
    g_diff=0
    h_diff=0
    for i in range(0,len(g_coeffs)):
      power = len(g_coeffs)-i-1
      g+=g_coeffs[i]*(x**power)
      if power>0:
        g_diff+=power*g_coeffs[i]*(x**(power-1))
    for i in range(0,len(h_coeffs)):
      power = len(h_coeffs)-i-1
      h+=h_coeffs[i]*(x**power)
      if power>0:
        h_diff+=power*h_coeffs[i]*(x**(power-1))

    quotient = ((h*g_diff)-(h_diff*g))/(h**2)

    return quotient

