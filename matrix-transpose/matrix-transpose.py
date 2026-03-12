import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    B = np.zeros((len(A[0]),len(A)),dtype = np.int16)
    A = np.array(A)
    for i in range(len(A)):
        for j in range(len(B)):
            B[j][i] = A[i][j]
    
    return B
    pass
