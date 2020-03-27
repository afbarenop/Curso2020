x=2
X=2
C=0
while(x < 90000):
    s=x
    c=0
    while (s != 1):
        if (s%2 == 0):
            s = s/2
        else:
            s = 3*s+1
        c=c+1
    if (C <= c):
        C=c
        X=x
    x = x+1
print(C)
print(X)