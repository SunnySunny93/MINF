# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:07:32 2016

@author: Abk739
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.signal import convolve2d

eingangsbild = r"enter_dirty.png" #raw strings (verhindern Formatierung)
ausgangsbild = "cleaned.png"

def clean(eingangsbild, ausgangsbild):
    bild = np.array(Image.open(eingangsbild))
    bildBW = np.array(Image.open(eingangsbild).convert("L"))
    ermittelGrau(bildBW, findeRGB(bild, bildBW))
    #findeRGB(bild,bildBW)
    plt.imshow(bildBW, cmap=cm.gray) 
    plt.imsave(ausgangsbild, bildBW, cmap =cm.gray)
    #plt.imshow(bildBW, cmap=cm.gray)
    #print(bild[1])
   
def findeRGB(bild,bildBW):
    height, width = bildBW.shape
    L = []
    for y in range(height):
        for x in range(width):
            pixel=bild[y,x]
            if(pixel[0] != pixel[1] or pixel[0] != pixel[2] or pixel[1] != pixel[2]): #Alle Pixel herausfinden, die nicht Grau sind.
                bildBW[y,x]= 0
                L = L + [[y,x]]            
    return L
def ermittelGrau(bildBW, L):
    height, width = bildBW.shape
    grau=0
    for durchgaenge in range(10):
        for i in range(len(L)):
            y,x = L[i]
            werte=0
            for j in range(-1,1):
                for k in range(-1,1):
                    if((j != 0) & (k != 0) & (bildBW[y+j,x+k] != 0)):
                        grau = grau + bildBW[y+j,x+k]
                        werte = werte +1
                        #print(werte)
            bildBW[y,x]=((grau)//werte)





clean(eingangsbild, ausgangsbild)