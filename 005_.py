# -*- coding: utf8 -*-

# 在数组中找到第k大的元素 :
# 给出数组 [9,3,2,4,8]，第三大的元素是 4
# 给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推

#   解法1： 我们可以对这个乱序数组按照从大到小先行排序，然后取出前k大，总的时间复杂度为O(n*logn + k)。
#   解法2： 利用选择排序或交互排序，K次选择后即可得到第k大的数。总的时间复杂度为O(n*k)
#   解法3： 利用快速排序的思想，从数组S中随机找出一个元素X，把数组分为两部分Sa和Sb。Sa中的元素大于等于X，Sb中元素小于X。这时有两种情况：
#        1. Sa中元素的个数小于k，则Sb中的第k-|Sa|个元素即为第k大数；
#        2. Sa中元素的个数大于等于k，则返回Sa中的第k大数。时间复杂度近似为O(n)
#   解法4： 二分[Smin,Smax]查找结果X，统计X在数组中出现，且整个数组中比X大的数目为k-1的数即为第k大数。时间复杂度平均情况为O(n*logn)
#   解法5：用O(4*n)的方法对原数组建最大堆，然后pop出k次即可。时间复杂度为O(4*n + k*logn)
#   解法6：维护一个k大小的最小堆，对于数组中的每一个元素判断与堆顶的大小，若堆顶较大，则不管，否则，弹出堆顶，将当前值插入到堆中。时间复杂度O(n * logk)
#   解法7：利用hash保存数组中元素Si出现的次数，利用计数排序的思想，线性从大到小扫描过程中，前面有k-1个数则为第k大数，平均情况下时间复杂度O(n)

########################################
# 1.
def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    return start


def kthLargestElement(k, alist):
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return

    start = 0
    end = length - 1
    index = partition(alist, start, end)
    while index != k:
        if index > k:
            index = partition(alist, start, index - 1)
        elif index < k:
            index = partition(alist, index + 1, end)
    return alist[:k]

########################################
# 2.
import heapq

# 大顶堆
def get_least_numbers_big_data(alist, k):
    max_heap = []
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return
    k = k - 1
    for ele in alist:
        if len(max_heap) <= k:
            heapq.heappush(max_heap, ele)
        else:
            # 判断添加元素值与堆的第一个元素值对比,如果大于则删除最小元素，然后添加新的元素值，否则不更改堆
            heapq.heappushpop(max_heap, ele)

    return max_heap

########################################
# 3.
k=3
list=[5,8,0,3,6,7,9,1,4,2]
import heapq
heapq.nlargest(k, list)


'''
# 计数排序
def countingSort(alist, k):
    n = len(alist)
    # 输出
    b = [0 for i in xrange(n)]
    # 空间占用
    c = [0 for i in xrange(k + 1)]

    for i in alist:
        c[i] += 1
    for i in xrange(1, len(c)):
        c[i] = c[i - 1] + c[i]

    for i in alist:
        b[c[i] - 1] = i
        c[i] -= 1
    print b
'''

# print(kthLargestElement(1, [1, 4, 5, 6, 10, 2, 0, 5]))
print(get_least_numbers_big_data([1, 4, 5, 6, 10, 2, 0, 5], 3))