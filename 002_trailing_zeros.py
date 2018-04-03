# -*- coding: utf8 -*-

# 尾部的零
# 设计一个算法，计算出n阶乘中尾部零的个数

def trailingZeros(n):
    '''
    >>> trailingZeros(5)
    1
    '''
    count = 0
    tmp = n // 5
    while tmp != 0:
        count += tmp
        tmp //= 5

    return count


# python -m doctest -v 002_trailing_zeros.py