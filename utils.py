def MSE(y, y_hat):
    """
    Compute mean squared error.
    See: https://en.wikipedia.org/wiki/Mean_squared_error
    Args:
        y (numpy 1d array of floats): actual values of data.
        y_hat (numpy 1d array of floats): estimated values via model.
    Returns:
        ecm (float): mean squared error result.
    """
    sum_res = 0
    for m in range(len(y)):
        sum_res += (y[m] - y_hat[m])**2
    return 1/len(y)*sum_res