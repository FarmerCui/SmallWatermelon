import random
import time


def quick_sort(data: []):
    """
    快速排序
    :param data:
    :return:
    """
    __data = data.copy()

    def inner_sort(start: int, end: int):
        stand = start
        for i in range(start, end + 1):
            if i == stand:
                continue
            if i < stand and __data[i] > __data[stand]:
                __data[i], __data[stand] = __data[stand], __data[i]
                stand = i
            elif i > stand and __data[i] < __data[stand]:
                if i - stand == 1:
                    __data[i], __data[stand] = __data[stand], __data[i]
                    stand = i
                else:
                    __data[stand], __data[stand + 1], __data[i] = \
                        __data[i], __data[stand], __data[stand + 1]
                    stand = stand + 1
        if start < stand:
            inner_sort(start, stand)
        if stand + 1 < end:
            inner_sort(stand + 1, end)

    inner_sort(0, len(__data) - 1)
    return __data


if __name__ == '__main__':
    """
    测试脚本
    """
    _data = [i for i in range(1000000)]
    random.shuffle(_data)
    t = time.time()
    quick_sort(_data)
    print('finished:', time.time() - t)
