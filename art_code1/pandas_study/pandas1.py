# -*- coding: utf-8 -*-
import pandas


if __name__ == '__main__':
    pan = pandas.read_csv("world.csv")
    print type(pan)
    print pan.columns
    aa = ['882','3']
    print pan[aa]