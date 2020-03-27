import numpy as np

sigma= 16
mu = 8
a = float(input ("Ingrese limite inferior >"))
b= float(input ("Ingrese limite superior > "))
dx= 0.005
x=a
S=0

def Gauss(x):
    X = pow(sigma*np.sqrt(2*np.pi),-1)*np.exp(-pow(x-mu,2)/(2*sigma**2))
    return X


while (a <= x <= b):
    y= Gauss(x)
    S= S+ y*dx
    x=x+dx

print(S)

