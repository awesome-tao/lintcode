# -*- coding: utf8 -*-
# 两个数相加,不使用+


# 比较讨巧的办法
def two_sum_1(a, b):
    return a - (-b)


# 位操作
def tow_sum_2(a, b):
    '''
    >>> tow_sum_2(1, 5)
    6
    '''
    if a == 0:
        return b

    if b == 0:
        return a

    sum = 0
    while b != 0:
        sum = a ^ b
        b = (a & b) << 1
        a = sum

    return sum


# 位操作,溢出


# python -m doctest -v 001_two_sum.py
