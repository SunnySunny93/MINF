# -*- coding: utf-8 -*-
import numpy as np

def decode(matrix1, matrix2):
    spalten = len(matrix1)
    zeilen = len(matrix2)
    if(spalten==zeilen):
        a=np.full((spalten,zeilen), -1, dtype=int)
 
        
        for n in range(5):
            eindeutig(matrix1, matrix2, a)
            weiter(matrix1, matrix2, a)
       
        #print(a)
        print(summe(a, spalten, spalten))
        return (summe(a, spalten, spalten))
    else:
        print("Eingabefehler")

def eindeutig(matrix1, matrix2, a):
    #print("Eindeutig")    
    spalten = len(matrix1)
    #füllen
    for i in range(spalten):
        for j in range(spalten):
            #print(matrix1[i])
            #Alles oder nichts
            if(spalten in matrix2[i]):
                a[j,i]=1
            if(0 in matrix2[i]):
                a[j,i]=0
            if(spalten in matrix1[j]):
                a[j,i]=1
            if(0 in matrix1[j]):
                a[j,i]=0
            #(2,1) oder (1,2)
            if((len(matrix2[i])>1)&((sum(matrix2[i])+((len(matrix2[i])-1)))==spalten)):
                b=matrix2[i]
                if(b[0]>b[1]):
                    for posi in range(b[0]):
                        a[posi,i]=1
                    a[spalten-1,i]=1
                else:
                    for posi in range(b[1]):
                        a[spalten-1-posi,i]=1
                    a[0,i]=1
            #(2,1) oder (1,2)
            if((len(matrix1[j])>1)&((sum(matrix1[j])+((len(matrix1[j])-1)))==spalten)):
                b=matrix1[j]
                if(b[0]>b[1]):
                    for posi in range(b[0]):
                        a[j,posi]=1
                    a[j,spalten-1]=1
                else:
                    for posi in range(b[1]):
                        a[j,spalten-1-posi]=1
                    a[j,0]=1
                    
            
    #print("Eindeutig:")
    pruefen(matrix1, matrix2, a)
    
def weiter(matrix1, matrix2, a):
    #print(a,"blubb")
    #print("weiter")
    #Spalten -1 bis 0 +1 mit einsen füllen
    spalten = len(matrix1)
    """n=spalten
    for do in range(n):
        for i in range(spalten):
            for j in range(spalten):
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[0,i] == 1)):
                    for posi in range(n-1):
                        if(a[posi,i]!=0):
                            a[posi,i] = 1
                if((((len(matrix2[i]))==1))&((n) in matrix2[i])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        if(a[spalten - 1 - (posi+1),i]!=0):
                            a[spalten - 1 - (posi+1),i] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[j,0] == 1)):
                    for posi in range(n-1):
                        if(a[j,posi]!=0):
                            a[j,posi] = 1
                if((((len(matrix1[j]))==1))&((n) in matrix1[j])&(a[spalten-1,i] == 1)):
                    for posi in range(n-1):
                        if(a[j, spalten - 1 - (posi+1)]!=0):
                            a[j, spalten - 1 - (posi+1)] = 1  
        n = n - 1"""
    #print(a)
    #print("Weiter1")
    pruefen(matrix1, matrix2, a)
    #Passt eine Kette in die Felder, wenn nicht Nullen setzen
    for i in range(spalten):
        for j in range(spalten):
            for n in range(spalten):
                if(n > spalten//2):
                    d=n
                    #print(d)
                    if(d in matrix2[i]):
                        if(a[0+(d-1), i]==-1):
                            a[0+(d-1), i]=1
                        if(a[spalten-(d), i]==-1):
                            a[spalten-(d), i]=1  
                    if(d in matrix1[j]):
                        if(a[j, 0+(d-1)]==-1):
                            a[j, 0+(d-1)]=1
                        if(a[j, spalten-(d)]==-1):
                            a[j, spalten-(d)]=1
    #print("Weiter2")
    pruefen(matrix1, matrix2, a)
    
    """for i in range(spalten):
        for j in range(spalten):
            n=spalten//2
            if(matrix2[i]==n):
                for j in range(spalten):
                    if(a[i,j]==1):
                        
            if(matrix1[j]==n):"""
            
    for i in range(spalten):
        n= spalten//2
        if(n in matrix2[i]):
            for j in range(spalten-1):
                if(a[j,i]!=1 & a[j+1,i]!=1):
                    if(a[j,i]==-1):
                        a[j,i]=0
    for j in range(spalten):
        n= spalten//2
        if(n in matrix1[j]):
            for i in range(spalten-1):
                if(a[j,i]!=1 & a[j,i+1]!=1):
                    if(a[j,i]==-1):
                        a[j,i]=0
    
    
    
    pruefen(matrix1, matrix2, a)      
    #print("B", a)
    #print("weiter3")

    #print(a,"blub")
    #Zellen ausschließen
    for i in range(spalten):
        for j in range(spalten):      
            if(((len(matrix2[i]))==1)&(a[j,i]==1)):
                c= matrix2[i][0]
                if((j-c)>=0):
                    if(a[j-c,i]==-1):
                        a[j-c,i]=0
                if((j+c)<=spalten-1):
                    if(a[j+c,i]==-1):
                        a[j+c,i]=0
                #print(b)
            if(((len(matrix1[j]))==1)&(a[j,i]==1)):
                b= matrix1[j][0]
                if((i-b)>=0):
                    if(a[j,i-b]==-1):
                        a[j,i-b]=0
                if((i+b)<=spalten-1):
                    if(a[j,i+b]==-1):
                        a[j,i+b]=0
                    #print(c)              
    #print("Weiter4")
    #print("a",a)         
    pruefen(matrix1, matrix2, a)
     
    
def pruefen(matrix1, matrix2, a):
    spalten = len(matrix1)
    #print("Prüfen")    
    #Kontrolle ob genug Einsen da sind
    #|
    #v
    for i in range(spalten):
        b=0
        for j in range(spalten):
            if(a[j,i]!=-1):
                b= b+a[j,i]
            if(b==sum(matrix2[i])):
                #print("True")
                for j in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=0
    #->
    for j in range(spalten):
        b=0
        for i in range(spalten):  
            if(a[j,i]!=-1):
                b= b+a[j,i]
            if(b==sum(matrix1[j])):
                #print("True")
                for i in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=0
        
    #Kontrolle ob genug Nullen da sind
    #|
    #v
    for i in range(spalten):
        b=0
        for j in range(spalten):
            if(a[j,i]==0):
                b= b+1
            if(b==spalten-sum(matrix2[i])):
                #print("True")
                for j in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=1
    #->
    for j in range(spalten):
        b=0
        for i in range(spalten):  
            if(a[j,i]==0):
                b= b+1
            #print(b,"==",spalten-sum(matrix1[j]))
            if(b==spalten-sum(matrix1[j])):
                #print("True")
                for i in range(spalten):
                    if(a[j,i]==-1):
                        a[j,i]=1
    
    for i in range(spalten):
        for j in range(spalten):
            if(matrix2[i]==[1,1]):
                #print("(1,1)")
                if(a[0,i]==1):
                    a[1,i]=0
                if(a[spalten-1,i]==1):
                    a[spalten-2,i]=0
                if(a[j,i]==1):
                    if((j-1)>=0):
                        a[j-1,i]=0
                    if((j+1)<=spalten-1):
                        a[j+1,i]=0
            if(matrix1[j]==[1,1]):
                #print("(1,1)")
                if(a[j,0]==1):
                    a[j,1]=0
                if(a[j,spalten-1]==1):
                    a[j,spalten-2]=0
                if(a[j,i]==1):
                    if((i-1)>=0):
                        a[j,i-1]=0
                    if((i+1)<=spalten-1):
                        a[j,i+1]=0
   
       
def summe(a, spalten, zeilen):
    b = np.reshape(a,( 1, zeilen*spalten))
    r = b[0]
    summe=0
    for i in range(len(r)):
        summe = summe + r[i]*2**i
    return summe



testSpecs = []

# Programm zum Testen Ihrer Funktion "decode"
def test (specs = testSpecs):
    anzahl=0
    fehler=0
    for n, rowSpec, colSpec in specs:
        anzahl= anzahl + 1
        print(n, end = ": ")
        if decode(rowSpec, colSpec) != n:
            fehler= fehler + 1
            print("Fehler!")
        else:
            print("OK")
    print("Anzahl: ", anzahl, " Fehler: ", fehler)

testSpecs = [
    (5, [[1], [1]], [[2], []]),
    (15, [[2], [2]], [[2], [2]]),
    (1, [[1], []], [[1], []]),
    (0, [[], []], [[], []]),
    (4, [[], [1]], [[1], []]),
    (42, [[1], [1, 1], []], [[1], [1], [1]]),
    (511, [[3], [3], [3]], [[3], [3], [3]]),
    (1, [[1], [], []], [[1], [], []]),
    (0, [[], [], []], [[], [], []]),
    (256, [[], [], [1]], [[], [], [1]]),
    (23, [[3], [1], []], [[1], [2], [1]]),
    (42, [[1, 1], [1], [], []], [[], [2], [], [1]]),
    (27094, [[2], [1, 2], [1, 1], [2]], [[2], [1, 1], [2, 1], [2]]),
    (59226, [[1, 1], [1, 1], [3], [3]], [[2], [1, 2], [3], [1, 1]]),
    (52984, [[1], [4], [3], [2]], [[1], [2], [3], [4]]),
    (26467, [[2], [2], [3], [2]], [[1, 1], [4], [3], []]),
    (7095, [[3], [2, 1], [2, 1], [1]], [[4], [3], [1], [2]]),
    (20408, [[1], [2, 1], [4], [1]], [[2], [2], [2], [3]]),
    (5661, [[1, 2], [1], [2], [1]], [[2, 1], [1], [1, 1], [1]]),
    (24431, [[4], [2], [4], [1, 1]], [[1, 2], [3], [4], [1, 1]]),
    (31222, [[2], [4], [1, 1], [3]], [[3], [2, 1], [2, 1], [2]]),
    (25012, [[1], [2, 1], [1], [2]], [[2], [1, 1], [1, 1], [1]]),
    (20909, [[1, 2], [1, 1], [1], [1, 1]], [[1, 2], [1], [1, 1], [2]]),
    (44633, [[1, 1], [1, 1], [3], [1, 1]], [[2], [2], [2], [1, 2]]),
    (45234, [[1], [2, 1], [], [2, 1]], [[1, 1], [2, 1], [], [1, 1]]),
    (34891, [[2, 1], [1], [1], [1]], [[1], [1], [1], [1, 2]]),
    (15472, [[], [3], [2], [2]], [[1, 1], [1, 1], [2], [1]]),
    (58591, [[4], [1, 2], [1], [3]], [[2], [1, 1], [4], [2, 1]]),
    (59478, [[2], [1, 1], [1], [3]], [[1], [1, 1], [2, 1], [2]]),
    (60237, [[1, 2], [1], [2, 1], [3]], [[1, 1], [2], [2, 1], [1, 2]]),
    (61339, [[2, 1], [1, 1], [4], [3]], [[3], [1, 2], [2], [4]]),
    (65238, [[2], [1, 2], [3], [4]], [[1, 1], [1, 2], [4], [3]]),
    (4469, [[1, 1], [3], [1], [1]], [[4], [1], [2], []]),
    (20683, [[2, 1], [2], [], [1, 1]], [[1, 1], [1], [1, 1], [2]]),
    (51775, [[4], [2], [1, 1], [2]], [[2], [3], [1, 1], [1, 2]]),
    (41135, [[4], [1, 1], [], [1, 1]], [[1], [2, 1], [1], [2, 1]]),
    (7198, [[3], [1], [2], [1]], [[1, 1], [1], [1, 1], [1, 1]]),
    (62398, [[3], [2, 1], [2], [4]], [[3], [4], [1, 1], [2, 1]]),
    (46377, [[1, 1], [1], [1, 1], [2, 1]], [[1, 2], [1, 1], [1], [1, 1]]),
    (45316, [[1], [], [1], [2, 1]], [[2], [1], [1], [1]]),
    (55343, [[4], [1], [1], [1, 2]], [[1, 1], [2], [1, 1], [1, 2]]),
    (15194, [[1, 1], [1, 1], [2, 1], [2]], [[3], [1, 2], [1], [1, 1]]),
    (30243, [[2], [1], [2], [3]], [[1, 1], [4], [2], []]),
    (38315, [[2, 1], [1, 1], [1, 1], [1, 1]], [[1, 2], [2], [1], [2, 1]]),
    (34621, [[1, 2], [2], [3], [1]], [[3], [2], [1, 1], [1, 1]]),
    (44215, [[3], [2, 1], [2], [1, 1]], [[2], [2, 1], [1, 1], [3]]),
    (7483, [[2, 1], [2], [1, 2], [1]], [[4], [2], [1], [1, 1]]),
    (27535, [[4], [1], [2, 1], [2]], [[1, 1], [1, 2], [1, 1], [3]]),
    (51971, [[2], [], [2, 1], [2]], [[1, 1], [1, 1], [1], [2]]),
    (5072, [[], [1, 2], [2], [1]], [[3], [1], [1], [1]]),
    (46191, [[4], [2], [1], [2, 1]], [[1, 1], [2, 1], [3], [1, 1]]),
    (11569, [[1], [2], [1, 2], [1]], [[3], [1, 1], [1], [1]]),
    (61885, [[1, 2], [2, 1], [1], [4]], [[4], [1, 1], [1, 1], [2, 1]]),
    (45550, [[3], [3], [1], [2, 1]], [[2], [2, 1], [2], [2, 1]]),
    (55892, [[1], [1, 1], [1, 1], [1, 2]], [[1, 1], [1], [2, 1], [2]]),
    (56146, [[1], [1, 1], [2, 1], [1, 2]], [[3], [1, 1], [1, 1], [2]])
]

# falls Sie eine Herausforderung suchen, probieren Sie die hier aus;
# mit: test(moreSpecs)

moreSpecs = [
    (28064727, [[3, 1], [4], [3], [2], [1, 2]], [[1], [3, 1], [3], [4], [2, 2]]),
    (33074501, [[1, 1], [1, 1], [2, 1], [1, 1], [5]], [[1, 3], [2, 1], [1, 1], [2, 1], [2]]),
    (23955595, [[2, 1], [1], [1], [2, 2], [2, 1]], [[1, 1], [1, 3], [1, 1], [1, 1], [2]]),
    (25995647, [[5], [2, 1], [1, 1], [1, 2], [2]], [[2, 1], [3], [1], [5], [1, 2]]),
    (11616024, [[2], [2], [4], [1], [2, 1]], [[1, 1], [3], [1], [3, 1], [2]]),
    (30620802, [[1], [1], [4], [2], [1, 3]], [[1, 1], [1, 2], [4], [1, 1], [1]]),
    (25817160, [[1], [1], [3], [2, 1], [2]], [[1], [1, 1], [1], [1, 1, 1], [3]]),
    (42, [[1, 1, 1], [], [], [], [], []], [[], [1], [], [1], [], [1]]),
    (23073092179, [[2, 1], [1, 1], [3, 2], [1], [5], [1, 1, 1]], [[3, 2], [1, 1, 1], [1, 2], [1, 1], [1, 4], [1]]),
    (66600934858, [[1, 1], [3, 2], [1, 2], [3, 1], [1], [5]], [[2, 1], [2, 1, 1], [1, 1, 1], [1, 2, 1], [2, 1], [1, 1, 1]]),
    (48182604456, [[1, 1], [1, 1], [2], [1, 3], [3, 2], [2, 1]], [[1, 1], [4], [2], [2, 1, 1], [2], [1, 3]]),
    (4242424242, [[1, 2], [2], [1, 4], [2, 2], [4], [], []], [[2, 1], [2, 2], [2], [1, 1], [1, 1], [1, 2], [2]]),
    (282566243037838, [[3], [1, 1, 2], [1, 1, 1], [1, 1], [1, 2], [5], [1]], [[1, 2], [1, 1, 1], [2, 1, 1], [1, 1, 1], [1], [4], [1, 1, 1]]),
    (40309940776018, [[1, 1, 1], [2, 1], [1, 2, 1], [1, 3], [2, 1], [1, 1, 1], [1, 1]], [[2, 2], [1, 1], [4], [3, 1], [2, 3], [], [3]]),
    (123389244652509, [[1, 3, 1], [3, 3], [1, 2], [2], [2], [3], [3]], [[2, 1], [2, 1], [2, 3], [1, 1, 1], [2, 1], [3], [4]]),
    (42424242424242, [[1, 2, 1], [1, 1, 1], [2, 3], [1, 1, 1, 1], [1, 1, 1, 1], [2, 1], [], []], [[1, 2], [1, 1, 1], [1, 2], [1, 1], [1, 1], [1, 2, 1], [2], [1, 3]]),
    (7345055201042728444, [[6], [1, 1, 1], [1, 1, 2], [1, 1], [1, 1, 2], [3], [3, 3], [1, 1, 2]], [[3, 1], [1, 1], [2, 2], [1, 1, 1, 1], [1], [1, 1, 3], [1, 1, 4], [3, 3]]),
    (3188175357875501851, [[2, 2], [2, 3, 1], [1, 1, 2], [3, 1, 1], [2, 1], [2, 1, 1], [5], [2, 1]], [[2, 1], [4, 1], [1, 3], [2, 4], [3, 1, 1], [1, 1, 3], [1], [5]]),
    (16103999649869894169, [[1, 2], [1, 1, 1], [1, 1], [1, 3], [2, 2, 1], [2, 3], [5], [5, 2]], [[1, 2, 1], [2, 2, 1], [3], [1, 1, 2], [2, 1, 2], [1, 2], [5], [3, 1, 1]])
]

test(specs = testSpecs)