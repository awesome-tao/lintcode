# -*- coding: utf8 -*-

# 合并两个排序的整数数组A和B变成一个新的数组。
# 给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]


def mergeSortedArray(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


# 归并排序
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) / 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return mergeSortedArray(left, right)


A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
print(mergeSortedArray(A, B))
