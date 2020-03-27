x=0
dx= 0.0000005
S=0
s=0
while (0<=x<=1):
    y= 4*(1-x**2)**(1/2)
    S= y*dx + S
    x = x + dx
x=dx
while (0<=x<=1):
    y= 4*(1-x**2)**(1/2)
    s= y*dx + s
    x = x + dx
print(S)
print(s)
