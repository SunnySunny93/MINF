# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:12:52 2016

@author: Anni
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

eingangsbild = r"000.png" #raw strings (verhindern Formatierung)

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
    return I
    
def ermittelSpieler(I, bild):
    spielerA = []   #Alle Steine von A
    spielerB = []   #Alle Steine von B
    felderA = []    #Nur die Felder
    felderB = []    #Nur die Felder
    leer=[]
    a=0
    for i in range(len(I)):
        feld, symbol, farbe = I[i]
        #print(I[i])
        if(symbol == 0):
            leer = leer + [feld]
        if(a==0) & (symbol != 0):
            spielerA = spielerA +I[i]
            aSymbol = spielerA[1]
            r, g, b = spielerA[2]
            felderA = felderA + [feld]
        if((a!=0)&(aSymbol==symbol)&(farbe[0]==r)&(farbe[1]==g)&(farbe[2]==b)):
            spielerA = spielerA + I[i]
            felderA = felderA + [feld]
        else:
            if((a!=0)&(symbol != 0)&(farbe[0]!=r)&(farbe[1]!=g)&(farbe[2]!=b)):
                spielerB = spielerB +I[i]
                felderB = felderB + [feld]
        a = a + 1
    #print(spielerA)
    #print(spielerB)
    zielkoord=gewinne(felderA, felderB, leer)
    print(zielkoord)
    
def gewinne(felderA, felderB, leer):
    if((len(felderA))<(len(felderB))):
        zug = felderA
    else:
        zug = felderB
    feld = loesung(zug, leer)
    spalte = int((feld-1) % 3)
    zeile = int((feld-1) // 3)
    return(zeile+1, spalte+1)
    
    
def loesung(zug, leer):
    
    diagonal = [[1,5,9],[3,5,7]]
    horizontal = [[1,2,3],[4,5,6],[7,8,9]]
    vertikal = [[1,4,7],[2,5,8],[3,6,9]]
    
    moeglichkeiten = diagonal + horizontal + vertikal
    for j in range(len(leer)):
        pruef = leer[j]
        zuga = []
        zuga = zug + [pruef]
        for i in range(len(moeglichkeiten)):
            pruef=moeglichkeiten[i]
            if((pruef[0] in zuga) & (pruef[1] in zuga) & (pruef[2] in zuga)):
                #print(leer[j])
                return(leer[j])
                break
    
solve(eingangsbild)