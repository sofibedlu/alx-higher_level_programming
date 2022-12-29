#!/usr/bin/python3
""" This module defines a function lazy_matrix_mul() while multiply
    two matrixes with NumpPy module
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrixes
        
        Args:
            m_a (list): the first matrix
            m_b (list): the second matrix
        Returns:
            the product of two matrix(m_a and m_b)
    """
    A = np.array(m_a)
    B = np.array(m_b)
    new_m = A.dot(B)
    return (new_m)
