# -*- coding: utf8 -*-

# 计算数字k在0到n中的出现的次数，k可能是0~9的一个值

def count_k(k, n):
    result = 0
    i = 1
    while n / i:
        cur = (n / i) % 10
        low = n - (n / i) * i
        high = n / (i * 10)

        if k == cur:
            result += high * i + low + 1
        elif k > cur:
            result += high * i
        else:
            result += (high + 1) * i

        i *= 10

    return result

# error
print(count_k(1, 12))
