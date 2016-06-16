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
    grau=0
    werte=0
    for i in range(len(L)):
        y,x = L[i]
        for i in range(-1,1):
            for j in range(-1,1):
                if bildBW[y+i,x+j] != 0:
                    grau = grau + bildBW[y+i,x+j]
                    werte = werte +1
        bildBW[y,x]=(grau/werte)
    return bildBW
clean(eingangsbild, ausgangsbild)