# 针对列表形式的数组进行快速排序
def fastsort(rawdata):
    # 基线条件
    if len(rawdata) < 2:
        return rawdata
    # 递归条件
    else:
        flag = rawdata.pop(random.randint(0, len(rawdata) - 1))
        upper = [i for i in rawdata if i >= flag]
        lower = [i for i in rawdata if i < flag]
        return fastsort(lower) + [flag] + fastsort(upper)


if __name__ == '__main__':
    import random
    import numpy as np

    # 产生随机数据
    numdata = 100
    rawdata = list(np.random.randint(1, 100, numdata).ravel())
    print(fastsort(rawdata))
