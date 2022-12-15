import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
# y=[2749.8525, 2639.52, 3044.0066999999995, 2824.3992, 2102.25, 2815.12, 2877.37, 2528.37, 2267, 2500, 2439, 2443, 2447, 2450]
x=[2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
y=[1950.25,1872,2158.87,2003.12,2102.25,2815.12,2877.37,2528.37,2267,2500,2439,2443,2447,2450]
ynew=[]
xnew=[]

for i in range(len(x)):
    pass
n=len(y)
print(n)
for i in range (n):
    q=np.arange(y[i]-5,y[i]+0.5,0.5)
    q1=np.arange(y[i]-0.5,y[i]-6,-0.5)
    w=np.arange(x[i]-0.1,x[i]+0.01,0.01)
    w1=np.arange(x[i]+0.01,x[i]+0.12,0.01)
    for j in range(len(q)):
        ynew.append(q[j])
        xnew.append(w[j])
    for j in range(len(q1)):
        ynew.append(q1[j])
        xnew.append(w1[j])



f2=interp1d(xnew,ynew,kind='cubic')
print(ynew)
print(f2(xnew))
plt.plot(xnew,f2(xnew))
plt.grid()
plt.show()