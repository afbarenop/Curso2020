x=1
y=2
w=1
M=1
while (w < 1000):
    while (y <= x):
        z= x%y
        if (z==0):
            if (y==x):
                M= ((x**2)/(x**2 - 1))*M
                w= w+1
            break
        y=y+1
    x=x+1
    y=2
MA= (6*M)**(1/2)
print(MA)



        