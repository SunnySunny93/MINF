# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:12:52 2016

@author: Anni
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

eingangsbild = r"092.png" #raw strings (verhindern Formatierung)

def solve(eingangsbild=eingangsbild):
    bild = np.array(Image.open(eingangsbild))
    bildBW = np.array(Image.open(eingangsbild).convert("L"))
    ermittelSpieler(inhalt(bild, bildBW), bild)
    plt.imshow(bild)    


#Erster Schritt: Felder analysieren. Symbole einheitlich färben
def inhalt(bild, bildBW):
    height, width = bildBW.shape
    drittelh = int(1/3*height)
    drittelb = int(1/3*width)
    #Einzelne Felder voneinander trennen.
    L=[[0, 0], [0, drittelb], [0, 2*drittelb], [drittelh, 0],[drittelh, drittelb], [drittelh, 2*drittelb], [2*drittelh, 0],[2*drittelh, drittelb], [2*drittelh, 2*drittelb]] 
    J=[]
    for i in range(len(L)):
        I=[]
        h,b=L[i]
        anzahlpixel=0
        #Analyse der Farbe
        for y in range(h+1,h + drittelh-1):             # +1 und -1 um die Linien auszuschließen
            for x in range(b+1, b + int(1/3*width)-1):
                if(bildBW[y,x] <= 240):
                    farbe = bild[y,x]
                    pixel = farbe[0], farbe[1], farbe[2]
                    I=I + [pixel]
        np.sort(I)
        f= (int)(len(I)/2)
        if(f != 0):
            t= I[f]
            #Mit neuer Farbe ausfüllen
            for y in range(h+1,h + drittelh-1):             # +1 und -1 um die Linien auszuschließen
                for x in range(b+1, b + int(1/3*width)-1):
                    if(bildBW[y,x] <= 240):
                        anzahlpixel= anzahlpixel + 1
                        bild[y,x] = t[0], t[1], t[2], 255
                        pixel = t[0], t[1], t[2]
                    else:
                        bild[y,x] = 255,255,255,255
        J=J+[[i+1, anzahlpixel, pixel]]
    return J

#2. Schritt: Felder den Spielern zuordnen. Dabei Farbe uns Symbol beachten
def ermittelSpieler(I, bild):
    spielerA = []   #Alle Steine von A
    spielerB = []   #Alle Steine von B
    felderA = []    #Nur die Felder
    felderB = []    #Nur die Felder
    leer=[]
    aSymbol=[]
    a=0
    for i in range(len(I)):
        feld, symbol, farbe = I[i]
        if(symbol == 0):
            leer = leer + [feld]
        else:
            if((a==0)):
                spielerA = spielerA +I[i]
                aSymbol = spielerA[1]
                r, g, b = spielerA[2]
                felderA = felderA + [feld]
                a = a + 1
            else:
                if((a!=0)&(aSymbol==symbol)&((farbe[0]==r)&(farbe[1]==g)&(farbe[2]==b))):
                    spielerA = spielerA + I[i]
                    felderA = felderA + [feld]
                else:
                    if(a != 0):
                        spielerB = spielerB +I[i]
                        felderB = felderB + [feld]
    zielkoord=gewinne(felderA, felderB, leer)
    print(zielkoord)
    
#Schritt 2.1: Einmittlung welcher Spieler am Zug ist
def gewinne(felderA, felderB, leer):
    if((len(felderA))<(len(felderB))):
        zug = felderA
    else:
        zug = felderB
    feld = loesung(zug, leer)
    spalte = int((feld-1) % 3)
    zeile = int((feld-1) // 3)
    return(zeile+1, spalte+1)
    
#Schritt 2.1.1: Gewinnmöglichkeiten werden geprüft
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
                return(leer[j])
                break
    
solve(eingangsbild)