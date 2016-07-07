# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 17:44:46 2016

@author: Anni
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.signal import convolve2d

matrix1 = [[1], [4], [3], [2]] 
matrix2 = [[1], [2], [3], [4]]

matrix1 = [[2], [1, 2], [1, 1], [2]]
matrix2 = [[2], [1, 1], [2, 1], [2]]

#matrix1 = [[1, 2], [1], [2, 1], [3]]
#matrix2 = [[1, 1], [2], [2, 1], [1, 2]]

#matrix1=[[1], [1]]
#matrix2=[[2], []]

#matrix1 = [[3], [1], [2], [1]]
#matrix2 = [[1, 1], [1], [1, 1], [1, 1]]

def decode(matrix1, matrix2):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    if(spalten==zeilen):
        a=np.full((spalten,zeilen), -1, dtype=int)
        for i in range(spalten):
            for j in range(spalten):
                if(a[j,i]==-1):
                    eindeutig(matrix1, matrix2, a)
                if(a[j,i]==-1):
                    weiter(matrix1, matrix2, a)
       
        print(a)
        print(summe(a, spalten, spalten))
        return (summe(a, spalten, spalten))
    else:
        print("Eingabefehler")

def eindeutig(matrix1, matrix2, a):
    spalten = len(matrix1)
    #füllen
    for i in range(spalten):
        for j in range(spalten):
            #print(matrix1[i])
            #Alles oder nichts
            if(spalten in matrix2[i]):
                a[j,i]=1
            if(0 in matrix2[i]):
                a[j,i]=0
            if(spalten in matrix1[j]):
                a[j,i]=1
            if(0 in matrix1[j]):
                a[j,i]=0
            #(2,1) oder (1,2)
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
            #(2,1) oder (1,2)
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
            if(matrix2[i]==[1,1]):
                for j in range(spalten):
                    if((a[j,i]==1)&(j<=spalten-2)):
                        a[j+1,i]=0
                    if((a[j,i]==1)&(j>1)):
                        a[j-1,i]=0
                    
                
                
                
                
                
                
    pruefen(matrix1, matrix2, a)
def weiter(matrix1, matrix2, a):
    #Spalten -1 bis 0 +1 mit einsen füllen
    spalten = len(matrix1)
    n=spalten
    for do in range(n):
        for i in range(spalten):
            for j in range(spalten):
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[0,i] == 1)):
                    for posi in range(n-1):
                        if(a[posi,i]!=0):
                            a[posi,i] = 1
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        if(a[spalten - 1 - (posi+1),i]!=0):
                            a[spalten - 1 - (posi+1),i] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[j,0] == 1)):
                    for posi in range(n-1):
                        if(a[j,posi]!=0):
                            a[j,posi] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        if(a[j, spalten - 1 - (posi+1)]!=0):
                            a[j, spalten - 1 - (posi+1)] = 1  
        n = n - 1     
    pruefen(matrix1, matrix2, a)
    #Passt eine Kette in die Felder, wenn nicht Nullen setzen
    for i in range(spalten):
        for j in range(spalten):
            for n in range(spalten):
                if(n > spalten//2):
                    d=n
                    #print(d)
                    if(d in matrix2[i]):
                        a[0+(d-1), i]=1
                        a[spalten-(d), i]=1  
                    if(d in matrix1[j]):
                        a[j, 0+(d-1)]=1
                        a[j, spalten-(d)]=1
    pruefen(matrix1, matrix2, a)
    for i in range(spalten):
        for j in range(spalten):
            n= spalten//2
            if(n in matrix2[i]):
                for j in range(spalten-1):
                    if(a[j,i]!=1 & a[j+1,i]!=1):
                        a[j,i]=0
            if(n in matrix1[j]):
                for i in range(spalten-1):
                    if(a[j,i]!=1 & a[j,i+1]!=1):
                        a[j,i]=0
    pruefen(matrix1, matrix2, a)
            
def pruefen(matrix1, matrix2, a):
    spalten = len(matrix1)
    #Kontrolle ob genug Einsen da sind
    #|
    #v
    for i in range(spalten):
        b=0
        for j in range(spalten):
            if(a[j,i]!=-1):
                b= b+a[j,i]
            if(b==sum(matrix2[i])):
                #print("True")
                for j in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=0
    #->
    for j in range(spalten):
        b=0
        for i in range(spalten):  
            if(a[j,i]!=-1):
                b= b+a[j,i]
            if(b==sum(matrix1[j])):
                #print("True")
                for i in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=0
    #Kontrolle ob genug Nullen da sind
    #|
    #v
    for i in range(spalten):
        b=0
        for j in range(spalten):
            if(a[j,i]==0):
                b= b+1
            if(b==spalten-sum(matrix2[i])):
                #print("True")
                for j in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=1
    #->
    for j in range(spalten):
        b=0
        for i in range(spalten):  
            if(a[j,i]==0):
                b= b+1
            if(b==spalten-sum(matrix1[j])):
                #print("True")
                for i in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=1
    print(a)










       
def summe(a, spalten, zeilen):
    b = np.reshape(a,( 1, zeilen*spalten))
    r = b[0]
    summe=0
    for i in range(len(r)):
        summe = summe + r[i]*2**i
    return summe


decode(matrix1, matrix2)
