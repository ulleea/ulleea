import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2+x-5

def count(f):
    def func(a):
        global k
        f(a)
        k+=1
        return f(a)
    return func

def dich(f, a,b,eps):
    c=(a+b)/2
    # while b-a>eps:

    while abs(f(a)-f(b))>eps:
        y=(a+c)/2

        if f(y)<=f(c):
            b=c
            c=y
        else:
            z=(c+b)/2

            if f(z)>=f(c):
                a=y
                b=z
                c=c
            else:
                a=c
                c=z
                b=b

    return a,b

def gold(f,a,b,eps):
    while abs(f(a)-f(b))>eps:
        y=a+0.382*(b-a)
        z=a+0.618*(b-a)
        if f(y)<=f(z):
            a=a
            b=z
            z=y
            y = a + 0.382 * (b - a)
        else:
            a=y
            b=b
            y=z
            z = a + 0.618 * (b - a)
    return a,b
#graph
a,b=-10,10
x=-10.2
arg,val=[],[]
for i in range(101):
    x+=0.2
    val.append(f(x))
    arg.append(x)
plt.plot(arg,val)
plt.grid()
plt.show()

#mins
a,b=-10,10
a,b=dich(f,a,b,0.005)
print((a+b)/2)
a,b=-10,10
a,b=gold(f,a,b,0.005)
print((a+b)/2)
print('----')
#decorator
k=0
a=-10
b=10
f=count(f)
a,b=dich(f,a,b,0.005)
print((a+b)/2)
print('колво вызовов= ',k)
k=0
a=-10
b=10
a,b=gold(f,a,b,0.005)
print((a+b)/2)
print('колво вызовов= ',k)
#correlation of eps
eps=0
vald=[]
valg=[]
arg=[]
for i in range(50):
    eps+=0.001
    arg.append(eps)
    k=0
    a, b = -10, 10
    a,b=dich(f,a,b,eps)
    vald.append(k)
    k = 0
    a, b = -10, 10
    a, b = gold(f, a, b, eps)
    valg.append(k)
plt.plot(arg,vald,color='red',label='dich')
plt.plot(arg,valg,color='blue',label='gold')
plt.legend()
plt.xlabel('eps')
plt.ylabel('number of using f')
plt.grid()
plt.show()