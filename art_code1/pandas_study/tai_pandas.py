# -*- coding: utf-8 -*-
import pandas


if __name__ == '__main__':
    pan = pandas.read_csv("train.csv")
    print pan.columns

    # 只要年龄的数据
    pan_age = pan['Age']

    # 获取年龄为空的索引
    null_res = pandas.isnull(pan_age)
    print null_res

    # 根据布尔索引得到具体的为空的数据
    print pan_age[null_res]
