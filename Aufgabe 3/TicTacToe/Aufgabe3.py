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
    inhalt= ermittelInhalt(bildBW, bild)
    ermittelSpieler(inhalt, bild)
    plt.imshow(bild)    
    
def ermittelInhalt(bildBW, bild):
    height, width = bildBW.shape
    drittelh = int(1/3*height)
    drittelb = int(1/3*width)
    L=[[0, 0], [0, drittelb], [0, 2*drittelb], [drittelh, 0],[drittelh, drittelb], [drittelh, 2*drittelb], [2*drittelh, 0],[2*drittelh, drittelb], [2*drittelh, 2*drittelb]]
    I=[]
    for i in range(len(L)):
        h,b=L[i]
        anzahlpixel=0
        farbe=0
        for y in range(h+1,h + drittelh-1):             # +1 und -1 um die Linien auszuschließen
            for x in range(b+1, b + int(1/3*width)-1):
                if(bildBW[y,x] != 255):
                    anzahlpixel= anzahlpixel + 1
                    farbe = bild[y,x]
                    pixel = farbe[0], farbe[1], farbe[2]
        I=I+[[i+1, anzahlpixel, pixel]]
    print(I)
    return I
    
def ermittelSpieler(I, bild):
    spielerA = []   #Alle Steine von A
    spielerB = []   #Alle Steine von B
    a=0
    for i in range(len(I)):
        feld, symbol, farbe = I[i]
        
        if(a==0) & (symbol != 0):
            spielerA = spielerA +I[i]
            aSymbol= spielerA[1]
            r, g, b= spielerA[2]
        #print(aSymbol)
        if((a!=0)&(aSymbol==symbol)&(farbe[0]==r)&(farbe[1]==g)&(farbe[2]==b)):
            spielerA = spielerA + I[i]
        else:
            if((a!=0)&(symbol != 0)&(farbe[0]!=r)):
                spielerB = spielerB +I[i]
        a = a + 1
    gewinne(spielerA, spielerB)
def gewinne(spielerA, spielerB):
    if(len(spielerA))<(len(spielerB))):
    
    

solve(eingangsbild)