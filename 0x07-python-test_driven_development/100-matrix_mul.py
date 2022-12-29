#!/usr/bin/python3
"""Module to find product of two matrix
"""


def matrix_mul(m_a, m_b):
    """function that computes product of two matrix
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(l_a, list) for l_a in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(l_b, list) for l_b in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or all(len(i) == 0 for i in m_a):
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0 or all(len(i) == 0 for i in m_b):
        raise TypeError("m_b can't be empty")
    if not all(isinstance(el, (int, float)) for l_a in m_a for el in l_a):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(el, (int, float)) for l_b in m_b for el in l_b):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(m_a[0]) == len(m_a[i]) for i in range(len(m_a))):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(m_b[0]) == len(m_b[i]) for i in range(len(m_b))):
        raise TypeError('each row of m_b must be of the same size')

    m_trans = []
    li = []
    for i in range(len(m_b[0])):
        for j in range(len(m_b)):
            li.append(m_b[j][i])
        m_trans.append(li)
        li = []
    """check for if it is not possible for the two matrix to multiplied
    """

    for i in range(len(m_a)):
        for j in range(len(m_trans)):
            if not len(m_a[i]) == len(m_trans[j]):
                raise ValueError("m_a and m_b can't be multiplied")
    mul = 1
    result = 0
    l_e = []
    m_p = []
    for i in range(len(m_a)):
        for k in range(len(m_trans)):
            list_k = m_trans[k]
            for j in range(len(m_trans[0])):
                mul = m_a[i][j] * list_k[j]
                result += mul
            l_e.append(result)
            result = 0
        m_p.append(l_e)
        l_e = []
    return m_p
