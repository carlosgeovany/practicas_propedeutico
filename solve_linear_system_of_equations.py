
def PLU(matrix, rhs):
    """
    Compute numerical approximation to linear system of equations Ax=b using
    factorization PLU via scipy.
    Args:
        matrix (numpy 2d array of floats): Square system matrix.
        rhs (numpy 1d array of floats): Right hand side of linear system of equations.
    Returns:
        x (numpy 1d array of floats or string): solution of Ax=b if A is square, if not returns string 
        "System matrix must be square"
    """
    import numpy as np
    from scipy.linalg import solve_triangular, lu

    if (matrix.shape[0] != matrix.shape[1]) or (matrix.shape == (1,1)):
        return "System matrix must be square"
    else:
        P, L, U = lu(matrix)
        D = solve_triangular(L,P@rhs,lower=True)
        return solve_triangular(U,D)

def QR(matrix, rhs):
    """
    Compute numerical approximation to linear system of equations Ax=b using
    factorization QR via numpy.
    Args:
        matrix (numpy 2d array of floats): Square system matrix.
        rhs (numpy 1d array of floats): Right hand side of linear system of equations.
    Returns:
        x (numpy 1d array of floats or string): solution of Ax=b if A is square, if not returns string 
        "System matrix must be square"
    """
    import numpy as np
    from scipy.linalg import solve_triangular

    if (matrix.shape[0] != matrix.shape[1]) or (matrix.shape == (1,1)):
        return "System matrix must be square"
    else:
        Q, R = np.linalg.qr(matrix)
        return solve_triangular(R, Q.T@rhs) 