#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
        '''Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
        Raises:
        ValueError: if m_a and m_b can not be multiplied.
        Exception: if error occured during multiplication.
    '''
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise Exception("An error occurred during matrix multiplication") from e
