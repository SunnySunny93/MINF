# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:07:32 2016

@author: Abk739
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def avgImg(start =1, end=1):
    plt.imshow(np.mean([np.array(Image.open("Aufgabe1/.jpg".format(i)).convert("L")) for i in range (start, end +1)], axis = 0), cmap=cm.gray)