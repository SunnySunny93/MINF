# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:12:52 2016

@author: Anni
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.signal import convolve2d

eingangsbild = r"000.png" #raw strings (verhindern Formatierung)
ausgangsbild = "000.png"

def solve(eingangsbild):
    bild = np.array(Image.open(eingangsbild))
    bildBW = np.array(Image.open(eingangsbild).convert("L"))
    
    ermittelInhalt(bildBW, bild)
    plt.imshow(bild)    
    
def ermittelInhalt(bildBW, bild):
    height, width = bildBW.shape
    L=[[0, 0], [1/3*width, 0], [2/3*width, 0], [0, 1/3*height],[1/3*width, 1/3*height], [2/3*width, 1/3*height],[0, 2/3*height],[1/3*width, 2/3*height],[2/3*width, 2/3*height]]
    for i in range(len(L)):
        for y in range(i[1], i[1]+(1/3*height)):
            for x in range(i[0], i[0]+(1/3*width)):
                if(bildBW[y,x] != 0):
                    bild[y,x] = [150,150,0,255]
                    
solve(eingangsbild)