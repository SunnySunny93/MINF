# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:40:05 2016

@author: Anni
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.signal import convolve2d

matrix1 = [[1], [4], [3], [2]] 
matrix2 = [[1], [2], [3], [4]]

def decode(matrix1, matrix2):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    print(spalten)
    print(zeilen)
    a = np.zeros((spalten, zeilen), dtype=np.int)
    #print(a)
    for i in range(spalten):
        for j in range(zeilen):
            print(matrix1[i])
            if(spalten in matrix1[i]):
                a[j,i]=1
            if(zeilen in matrix2[j]):
                a[j,i]=1
    print(a)

    

    #b = np.reshape(a, 1)


decode(matrix1, matrix2)

