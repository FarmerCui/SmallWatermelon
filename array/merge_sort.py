import random
import time
import math


def merge_sort(data: []) -> []:
    """
    归并排序
    """
    __data = data.copy()

    def swap(idx1: int, idx2: int):
        nonlocal __data
        __data[idx1], __data[idx2] = __data[idx2], __data[idx1]

    def recursion_merge(start: int, end: int):
        """
        递归方法实现
        1 3 5 7 10 2 4 6 8 9
        1 2 5 7 10 3 4 6 8 9
        1 2 3 7 10 5 4 6 8 9
        1 2 3 7 10 4 5 6 8 9 ...
        1 2 3 4 10 7 5 6 8 9
        1 2 3 4 10 5 6 7 8 9 ...
        1 2 3 4 5 10 6 7 8 9
        1 2 3 4 5 6 7 8 9 10 ...
        """
        if end - start == 1:
            if __data[start] > __data[end]:
                swap(start, end)
            return
        center = (end + start) // 2
        if start < center:
            recursion_merge(start, center)
        if center + 1 < end:
            recursion_merge(center + 1, end)
        right = center + 1
        for i in range(start, center + 1):
            if __data[i] > __data[right]:
                swap(i, right)
                for j in range(right, end):
                    if __data[j] > __data[j + 1]:
                        swap(j, j + 1)
                    else:
                        break

    recursion_merge(0, len(__data) - 1)
    return __data


if __name__ == '__main__':
    """
    测试脚本
    """
    _data = [i for i in range(50)]
    random.shuffle(_data)
    t = time.time()
    _data = merge_sort(_data)
    print(_data)
    print('finished:', time.time() - t)
