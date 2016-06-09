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
    findeRGB(bild, bildBW)
    plt.imshow(bild) 
    plt.imsave(ausgangsbild, bild)
    #plt.imshow(bildBW, cmap=cm.gray)
    #print(bild[1])
    
def findeRGB(bild,bildBW):
    height, width = bildBW.shape
    for y in range(height):
        for x in range(width):
            pixel=bild[y,x]
            if(pixel[0] != pixel[1] or pixel[0] != pixel[2] or pixel[1] != pixel[2]):
                bild[y,x]= [255,0,0, 255]
                """#pixel1 = bildBW[y,x]
                pixel2 = bildBW[y-1, x-1]
                #pixel3 = bildBW[y+1, x+1]
                pixel4 = bildBW[y, x-1]
                #pixel5 = bildBW[y, x+1]
                pixel6 = bildBW[y-1, x]
                #pixel7 = bildBW[y+1, x]
                #pixel8 = bildBW[y-1, x+1]
                #pixel9 = bildBW[y+1, x-1]
                durchschnitt = (pixel2 + pixel4 + pixel6 )/3
                bild[y,x]=durchschnitt"""
    #plt.imshow(bild)        
clean(eingangsbild, ausgangsbild)