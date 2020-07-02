from pytest import approx
import numpy as np

from utils import MSE

np.random.seed(1989) #for reproducibility
mpoints = 20
x = np.random.randn(mpoints) 
y = -3*x + np.random.normal(2,1,mpoints)
A=np.ones((mpoints,2))
A[:,1] = x
Q,R = np.linalg.qr(A)
beta = np.linalg.solve(R,Q.T@y)
y_hat_QR = A@beta

mse_approx = MSE(y, y_hat_QR)
mse_obj = 1.0217738419387945


def test_MSE():
    assert mse_approx == approx(mse_obj)
