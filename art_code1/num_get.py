# -*- coding: utf-8 -*-
# 查看 numpy 里面的数据


import numpy


if __name__ == '__main__':

    matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

    print matrix
    print '取某一个数据'
    print matrix[1, 1]
    print '取第二列的数据'
    print matrix[:, 1]
    print '取第一列和第二列的数据'
    print matrix[:, 0:2]
    print '取某些列和某些列的数据'
    print matrix[1:3, 0:2]







