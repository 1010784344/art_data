# -*- coding: utf-8 -*-
# numpy 函数


import numpy


if __name__ == '__main__':
    # numpy 数据类型转换
    vector = numpy.array(['1', '2', '3', '4'])
    print vector.dtype
    vector = vector.astype(float)
    print vector.dtype
    print vector

    # 对行求和
    matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
    print matrix.sum(axis=1)

    # 对列求和
    print matrix.sum(axis=0)
