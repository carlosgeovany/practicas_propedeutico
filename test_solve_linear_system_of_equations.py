from pytest import approx
import numpy as np

from solve_linear_system_of_equations import PLU, QR

#1.first excercise

#1.1first test
A_1_1 = np.array([
              [0, 1, -1],
              [-2, 4, -1],
              [-2, 5, -4]
              ], dtype=float)
b_1_1 = np.array([3, 1, -2], dtype=float)
x_plu_approx_1_1 = PLU(A_1_1, b_1_1)
x_qr_approx_1_1 = QR(A_1_1, b_1_1)
x_plu_obj_1_1 = np.array([10, 6, 3], dtype=float)
x_qr_obj_1_1 = np.array([10, 6, 3], dtype=float)

#1.2second test
A_1_2 = np.array([
              [0, 1, -1],
              [-2, 4, -1],
              [-2, 5, -4],
              [1, -1, 1]
              ], dtype=float)
b_1_2 = np.array([3, 1, -2, 0], dtype=float)
x_plu_approx_1_2 = PLU(A_1_2, b_1_2)
x_qr_approx_1_2 = QR(A_1_2, b_1_2)

#second excercise
#2.1first test
b_2_1 = np.array([-5, 7, 0], dtype=float)
x_plu_approx_2_1 = PLU(A_1_1, b_2_1)
x_qr_approx_2_1 = QR(A_1_1, b_2_1)
x_plu_obj_2_1 = np.array([-12, -4, 1], dtype=float)
x_qr_obj_2_1 = np.array([-12, -4, 1], dtype=float)

#2.2second test
b_2_2 = np.array([-5, 7, 0, 1])
x_plu_approx_2_2 = PLU(A_1_2, b_2_2)
x_qr_approx_2_2 = QR(A_1_2, b_2_2)

#first tests excercise 1
def test_plu_1_1():
    assert x_plu_approx_1_1 == approx(x_plu_obj_1_1)
def test_qr_1_1():
    assert x_qr_approx_1_1 == approx(x_qr_obj_1_1)
def test_plu_1_2():
    assert x_plu_approx_1_2 == "System matrix must be square"
def test_qr_1_2():
    assert x_qr_approx_1_2 == "System matrix must be square"
    
#second tests excercise 2

def test_plu_2_1():
    assert x_plu_approx_2_1 == approx(x_plu_obj_2_1)
def test_qr_2_1():
    assert x_qr_approx_2_1 == approx(x_qr_obj_2_1)
def test_plu_2_2():
    assert x_plu_approx_2_2 == "System matrix must be square"
def test_qr_2_2():
    assert x_qr_approx_2_2 == "System matrix must be square"
