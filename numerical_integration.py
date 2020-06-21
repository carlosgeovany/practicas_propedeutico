import numpy as np

def Tcf(f,a,b,n): #Tcf: composite trapezoidal method for f
    """
    Compute numerical approximation using trapezoidal method in 
    an interval.
    Nodes are generated via formula: x_i = a+ih_hat for i=0,1,...,n and h_hat=(b-a)/n
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    h_hat=(b-a)/n
    sum_res = 0
    for i in np.arange(n):
        x = a + (i*h_hat)
        sum_res+= f(x)
    return h_hat*sum_res

def GLf(f,a,b,n): #GLf: Gauss-Legendre quadrature for f
    """
    Compute numerical approximation using quadrature Gauss-Legendre.
    Weights and nodes are obtained with table for n=0,1,2,3,4
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    from scipy.special import p_roots
    [x,w] = p_roots(n+1)
    return (b-a)/2*sum(w*f((b-a)/2*x+(b+a)/2))

def GHf(f,mu, sigma): #GHf: Gauss-Hermite quadrature for f
    """
    Compute numerical approximation using quadrature Gauss-Hermite.
    Weights and nodes are obtained with table in Kiusalaas for n=6
    Args:
        f (function): function expression of integrand
        mu (float): mean
        sigma (float): standard deviation
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    from scipy.special import roots_hermite
    [x,w] = roots_hermite(5)
    return sum(1/np.sqrt(np.pi)*w*f(np.sqrt(2)*sigma*x+mu))