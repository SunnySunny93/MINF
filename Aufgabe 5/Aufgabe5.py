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

#matrix1 = [[1, 2], [1], [2, 1], [3]
#matrix2 = [[1, 1], [2], [2, 1], [1, 2]]

#matrix1=[[1], [1]]
#matrix2=[[2], []]

def decode(matrix1, matrix2):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    if(spalten==zeilen):
        #print(matrix1)
        #print(matrix2)
        a = np.zeros((spalten, spalten), dtype=np.int)
        #print(a)
        ganz(matrix1, matrix2, a)
        n=spalten
        f=0
        for i in range(len(matrix1)):
            if(i>1):
                n=n -1
                f = f + 1
                fuellen(matrix1, matrix2, a, n, f)
            print(f)
            
        #abDrei(matrix1, matrix2, a)
        #abVier(matrix1, matrix2, a)  
        print(a)
        print(summe(a, spalten, spalten))
    else:
        print("Eingabefehler")
    
def ganz(matrix1, matrix2, a):
    spalten = len(matrix1)
    for i in range(spalten):
        for j in range(spalten):
            #print(matrix1[i])
            if(spalten in matrix2[i]):
                a[j,i]=1
            if(spalten in matrix1[j]):
                a[j,i]=1
                
def fuellen(matrix1, matrix2, a, n, f):
    spalten = len(matrix1)
    b= n
    for i in range(spalten):
        for j in range(spalten):
            if((n-f) in matrix2[i]):
                if(a[0,i] == 1):
                    for posi in range(b):
                        a[posi,i] = 1
            if((n-f) in matrix2[i]):
                if(a[n,i] == 1):
                    for posi in range(b):
                        a[n - (posi+1),i] = 1
            if((n-f) in matrix1[j]):
                if(a[j,0] == 1):
                    for posi in range(b):
                        a[j,posi] = 1
            if((n-f) in matrix1[j]):
                if(a[n,i] == 1):
                    for posi in range(b):
                        a[j, n - (posi+1)] = 1               
    

def abVier(matrix1, matrix2, a):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    b = spalten -3
    for i in range(spalten):
        for j in range(zeilen):
            if((spalten -2) in matrix2[i]):
                if(a[0,i] == 1):
                    for posi in range(b):
                        a[posi,i] = 1
            if((spalten -2) in matrix2[i]):
                if(a[spalten-1,i] == 1):
                    for posi in range(b):
                        a[spalten - 1 - (posi+1),i] = 1
            if((zeilen -2) in matrix1[j]):
                if(a[j,0] == 1):
                    for posi in range(b):
                        a[j,posi] = 1
            if((zeilen -2) in matrix1[j]):
                if(a[zeilen-1,i] == 1):
                    for posi in range(b):
                        a[j, zeilen - 1 - (posi+1)] = 1   
  
def abDrei(matrix1, matrix2, a):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    b = spalten -2
    for i in range(spalten):
        for j in range(zeilen):
            if((spalten -1) in matrix2[i]):
                if(a[0,i] == 1):
                    for posi in range(b):
                        a[posi,i] = 1
            if((spalten -1) in matrix2[i]):
                if(a[spalten-1,i] == 1):
                    for posi in range(b):
                        a[spalten - 1 - (posi+1),i] = 1
            if((zeilen -1) in matrix1[j]):
                if(a[j,0] == 1):
                    for posi in range(b):
                        a[j,posi] = 1
            if((zeilen -1) in matrix1[j]):
                if(a[zeilen-1,i] == 1):
                    for posi in range(b):
                        a[j, zeilen - 1 - (posi+1)] = 1
          
def summe(a, spalten, zeilen):
    b = np.reshape(a,( 1, zeilen*spalten))
    r = b[0]
    summe=0
    for i in range(len(r)):
        summe = summe + r[i]*2**i
    return summe


decode(matrix1, matrix2)































