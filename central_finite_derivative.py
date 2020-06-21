def approx_first_derivative(f,x,h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate first derivative of function.
    Args:
        f (function): function definition.
        x (float): point where first derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        df (float): approximation to first_derivative.
    """
    df = (f(x+h) - f(x-h))/(2.0*h)
    return df

def approx_second_derivative(f,x,h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate second derivative of function.
    Args:
        f (function): function definition.
        x (float): point where second derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        df (float): approximation to second_derivative.
    """
    df =(f(x+h) - 2.0*f(x) + f(x-h))/h**2
    return df

def relative_absolute_error(aprox, obj):
    """
    Calculate the Relative Absolute Error. The magnitude of the difference between 
    the objective point and the approximation
    Args:
        aprox (float): point where second derivative was approximated
        obj (float): point where the function was evaluated. obj must be disticnt from zero
    Returns:
        (float): relative abosulote error.
    """    
    import numpy as np
    if(np.abs(obj) > 0 ):
        return np.abs(aprox-obj)/np.abs(obj)
    else:
        return np.abs(aprox-obj)