# -*- coding: utf-8 -*-

# 将其他数据加载到 numpy 里面

import numpy

if __name__ == '__main__':
    # 加载 txt 数据为 ndarry 对象
    # delimiter 代表分割符，dtype 默认以str 的方式读进来
    world = numpy.genfromtxt('world.txt', delimiter=',', dtype=str)
    print type(world)
    print world

    # 加载列表为 ndarry 对象
    # 一维
    vector = numpy.array([5, 10, 15, 20])
    print type(vector)
    print vector

    # 二维
    matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
    print type(matrix)
    print matrix

    # 查看 ndarry 的数据结构,对于一个矩阵，它的行和列分别等于多少
    print vector.shape
    print matrix.shape

    # 查看 ndarry 的数据类型
    print vector.dtype
    print matrix.dtype





