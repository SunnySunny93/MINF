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

#matrix1 = [[1], [4], [3], [2]] 
#matrix2 = [[1], [2], [3], [4]]

#matrix1 = [[1, 2], [1], [2, 1], [3]]
#matrix2 = [[1, 1], [2], [2, 1], [1, 2]]

#matrix1=[[1], [1]]
#matrix2=[[2], []]

matrix1 = [[3], [1], [2], [1]]
matrix2 = [[1, 1], [1], [1, 1], [1, 1]]

def decode(matrix1, matrix2):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    if(spalten==zeilen):
        #print(matrix1)
        #print(matrix2)
        a = np.zeros((spalten, spalten), dtype=np.int)
        #print(a)
        ganz(matrix1, matrix2, a)
       
        fuellen(matrix1, matrix2, a)
        test(matrix1, matrix2, a)
        #abDrei(matrix1, matrix2, a)
        #abVier(matrix1, matrix2, a)  
        print(a)
        print(summe(a, spalten, spalten))
        return (summe(a, spalten, spalten))
    else:
        print("Eingabefehler")
  

def test(mtarix1, matrix2, a):
    print(len(matrix1[0]))
    print(sum(matrix1[0])+((len(matrix1[0])-1)))
    kuckuk= matrix1[0]
    print(kuckuk[0])
    print("summe", sum(a[0]))
    
def ganz(matrix1, matrix2, a):
    spalten = len(matrix1)
    for i in range(spalten):
        for j in range(spalten):
            #print(matrix1[i])
            if(spalten in matrix2[i]):
                a[j,i]=1
            if(spalten in matrix1[j]):
                a[j,i]=1
            if((len(matrix2[i])>1)&((sum(matrix2[i])+((len(matrix2[i])-1)))==spalten)):
                b=matrix2[i]
                if(b[0]>b[1]):
                    for posi in range(b[0]):
                        a[posi,i]=1
                    a[spalten-1,i]=1
                else:
                    for posi in range(b[1]):
                        a[spalten-1-posi,i]=1
                    a[0,i]=1
            if((len(matrix1[j])>1)&((sum(matrix1[j])+((len(matrix1[j])-1)))==spalten)):
                b=matrix1[j]
                if(b[0]>b[1]):
                    for posi in range(b[0]):
                        a[j,posi]=1
                    a[j,spalten-1]=1
                else:
                    for posi in range(b[1]):
                        a[j,spalten-1-posi]=1
                    a[j,0]=1
                
def fuellen(matrix1, matrix2, a):
    spalten = len(matrix1)
    n=spalten
    for do in range(n):
        for i in range(spalten):
            for j in range(spalten):
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[0,i] == 1)):
                    for posi in range(n-1):
                        a[posi,i] = 1
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        a[spalten - 1 - (posi+1),i] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[j,0] == 1)):
                    for posi in range(n-1):
                        a[j,posi] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        a[j, spalten - 1 - (posi+1)] = 1  
        n = n - 1
    

"""def abVier(matrix1, matrix2, a):
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
                        a[j, zeilen - 1 - (posi+1)] = 1"""
          
def summe(a, spalten, zeilen):
    b = np.reshape(a,( 1, zeilen*spalten))
    r = b[0]
    summe=0
    for i in range(len(r)):
        summe = summe + r[i]*2**i
    return summe


decode(matrix1, matrix2)































