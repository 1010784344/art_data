# -*- coding: utf-8 -*-
# numpy == 判断值是否相等


import numpy


if __name__ == '__main__':

    # 判断 numpy 里面有没有一个值是等于一个数的
    vector = numpy.array([5, 10, 15, 20])
    result = (vector == 10)
    print result
    # [False  True False False]

    # 根据布尔值去取出对应的数据
    print vector[result]

    # 复杂的根据布尔值去取出对应的数据
    matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
    mul_res = (matrix[:, 1] == 25)
    print mul_res
    print matrix[mul_res, :]










