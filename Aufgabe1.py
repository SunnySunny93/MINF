# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:07:32 2016

@author: Abk739
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

eingangsbild= "/Aufgabe 1/enter_dirty.png"
ausgangsbild =0

def clean(eingangsbild, ausgangsbild):
    bild = np.array(Image.open(eingangsbild).convert("L"))
    print(bild)
    
clean(eingangsbild, ausgangsbild)