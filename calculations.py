import csv
from debug import *
from scipy import interpolate



def loadData(filename):

    with open('dane.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
       
        T=[]
        c=[]
        i=0
        for row in csv_reader:
            row=list(map(float,row))
            T.append(row[0])
            c.append(row[1])
            i+=1
        return T,c



def interpolation(T, q):
    f = interpolate.interp1d(T, q);
    T2=[]
    q2=[]
    i=int(T[0])
    while i<= int(T[-1]):
        T2.append(i);
        q2.append(f(i));
        i+=1;
    return T2,q2



def entalpia(T, c, Q=[]):

    H=[None]*len(T)
    if(not Q):
        H[0]=(T[1]-T[0])*(c[0]+c[1])/2
        for i in range(1, len(T)-1) :  
           H[i]= H[i-1]+(T[i+1]-T[i])*(c[i+1]+c[i])/2
    else:
        H[0]=(T[1]-T[0])*(c[0]+c[1])/2+Q[0] 
        for i in range(1, len(T)-1) :  
           H[i]= H[i-1]+(T[i+1]-T[i])*(c[i+1]+c[i])/2+Q[i]

    return H


def option1(T_min, T_max, Tp, Tk, dH):
    Q=[0]*(T_max-T_min)
    h=dH/(Tk-Tp)
    for i in range(Tp, Tk):
        Q[i]=h
    return Q







T,c = loadData("dane.txt")  #zczytywanie dsanych
T,c = interpolation(T, c)   #interpolowanie co 1 oC
H=entalpia(T, c);           #obliczanie entalpii
#wyświetlanie wykresu T,H


#załóżmy, że użytkownik chce dodać ciepło reakcji metodą 1:
Q=option1(T[0], T[-1], 800, 900, 200);  #sposób dodania ciepła reakcji, [zakres temperatur danych],[zakres temperatur reakcji],[ile ciepła dodać]
H=entalpia(T, c, Q);
#wyświetlanie wykresu T,H


