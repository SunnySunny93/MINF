# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:07:32 2016

@author: Abk739
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

eingangsbild = r"enter_dirty.png" #raw strings (verhindern Formatierung)
ausgangsbild = "cleaned.png"


def clean(eingangsbild=eingangsbild, ausgangsbild=ausgangsbild):
    bild = np.array(Image.open(eingangsbild))
    bildBW = np.array(Image.open(eingangsbild).convert("L"))
    L = findeRGB(bild, bildBW)
    schwelle(bildBW, L)
    ermittelGrau(bildBW, L)
    plt.imshow(bildBW, cmap=cm.gray)
    name=eingangsbild.split('_',1)
    ausgangsbild = "{}{}cleaned.png".format(name[0],"_")
    plt.imsave(ausgangsbild, bildBW, cmap =cm.gray)
   
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
    
def schwelle(bildBW, L):
    height, width = bildBW.shape
    for i in range(len(L)):
        y,x = L[i]
        grau = []
        for j in range(-1,2):
            for k in range(-1,2):
                if((y+j <= (height-1)) & (x+k <= (width-1))):
                    if(((j != 0) & (k != 0)) & (bildBW[y+j,x+k] != 0)):
                        grau = grau +[bildBW[y+j, x+k]]
        if((np.median(grau))>127):
            bildBW[y,x] = 255
        else:
            if((np.median(grau))<127):
                bildBW[y,x] = 0
            else:
                bildBW[y,x] = 127

def ermittelGrau(bildBW, L):
    height, width = bildBW.shape
    for durchgaenge in range(5):
        for i in range(len(L)):
            y,x = L[i]
            grau = [bildBW[y,x]]
            for j in range(-1,2):
                for k in range(-1,2):
                    if((y+j <= (height-1)) & (x+k <= (width-1))):
                        grau = grau +[bildBW[y+j, x+k]]
            bildBW[y,x]=int(np.median(grau))





clean("wtc_dirty.png", ausgangsbild)