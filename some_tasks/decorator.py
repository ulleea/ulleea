import numpy as np
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

# k=0
# f=count(f)
# # print(f(10))
# # print(k)
# # print(10**2+10-5)
# a=-10
# b=10
# a,b=dich(f,a,b,0.005)
# print((a+b)/2,k)
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
plt.show()
b = np.arange(27).reshape(3, 3,3)
a= (np.arange(27)*3).reshape(3, 3,3)
print(a)
print('---')
print(a[::2,::2,:])
# print(np.roll(b,1,axis=1))
# print(a)
# print(a-b)
# print(np.roll(b,1,axis=0))



