# -*- coding: utf8 -*-

# 设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
# 符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...


def nthUglyNumber(n):
    num_list = [1]
    i2 = i3 = i5 = 0
    while len(num_list) < n:
        num2, num3, num5 = num_list[i2] * 2, num_list[i3] * 3, num_list[i5] * 5
        # 上面一行比下面三行总耗时少
        #        num2 = num_list[i2] * 2
        #        num3 = num_list[i3] * 3
        #        num5 = num_list[i5] * 5
        num = min(num2, num3, num5)
        # 下面三个 if 还有去重的作用
        if num == num2:
            i2 += 1
        if num == num3:
            i3 += 1
        if num == num5:
            i5 += 1
        num_list.append(num)
    return num_list[-1]


print(nthUglyNumber(9))
