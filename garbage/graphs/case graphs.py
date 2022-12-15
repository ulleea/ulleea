import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
# y=[2749.8525, 2639.52, 3044.0066999999995, 2824.3992, 2102.25, 2815.12, 2877.37, 2528.37, 2267, 2500, 2439, 2443, 2447, 2450]
# x=[2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
#
# yzinc=[1950.25,1872,2158.87,2003.12,2102.25,2815.12,2877.37,2528.37,2267,2500,2439,2443,2447,2450]
# x=[12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#
# y=[]
#
# n=len(yzinc)
# print(n)
# for i in range(n):
#     if i==2:
#         y.append(yzinc[i]*1.41-200)#14
#     elif i==0:
#         y.append(yzinc[i]*1.41)
#     elif i == 3:
#         y.append(yzinc[i]*1.41+100)#15
#     elif i==4:
#         y.append(yzinc[i]*1.41-325)
#     elif i==5 :
#         y.append(yzinc[i]*1.41-320)
#     elif i==6:
#         y.append(yzinc[i]*1.41-310)#18
#     elif i==7:
#         y.append(yzinc[i]*1.41)
#     elif i==8:
#         y.append(yzinc[i]*1.41+300)
#     elif i==9:
#         y.append(yzinc[i]*1.41-150)
#     else:
#         y.append(yzinc[i]*1.41+random.randint(-20,30))
#     # y.append(yzinc[i] * (random.randint(132,142 )/100) + random.randint(-25, 20))
#     x[i]=x[i]+2000
# y[0]=y[0]-120
# ynew=[y[0]]
# xnew=[x[0]]
#
# for i in range(1,n-1):
#     a=y[i-1]-y[i]
#     b=y[i+1]-y[i]
#     q=[]
#     w=[]
#     # for j in range(10):
#     #     q.append(y[i]+a*0.005)
#     q=[y[i]+a*0.05,y[i]+a*0.025,y[i],y[i]+b*0.025,y[i]+b*0.05]
#     w=[x[i]-0.05,x[i]-0.025,x[i],x[i]+0.025,x[i]+0.05]
#     # print(x[i],y[i])
#     # print(q)
#     # print(w)
#     for j in range(5):
#         xnew.append(w[j])
#         ynew.append(q[j])
# xnew.append(x[-1])
# ynew.append(y[-1])
# print(xnew)
# # print(ynew)
# # plt.plot(xnew,ynew)
# # plt.grid()
# # plt.show()
# # for i in range (n):
# #     q=np.arange(y[i]-10,y[i]+11)
# #     ynew.append(q)
# #     w=np.arange(x[i]-0.1,x[i]+0.1)
# #     xnew.append(w)
# # print(len(x),len(y))
#
# y1=[y[9]]
# y2=[y[9]]
# y3=[yzinc[9]]
# y4=[yzinc[9]]
# for i in range(4):
#     # y1.append(y[9+i]+160+random.randint(-25,5))
#     # y2.append(y[9+i]-200+random.randint(-15,25))
#     y1.append(y[9 + i] + 160+random.randint(-15,15))
#     y2.append(y[9 + i] - 200 + random.randint(-15, 15))
# for i in range(4):
#     # y1.append(y[9+i]+160+random.randint(-25,5))
#     # y2.append(y[9+i]-200+random.randint(-15,25))
#     y3.append(yzinc[9 + i] + 160 + random.randint(-15,15))
#     y4.append(yzinc[9 + i] - 200 + random.randint(-15, 15))
# print(len(y1))
# print(x[9])
# f1=interp1d(x,yzinc,kind='cubic')
# f3=interp1d(x[9::],y1,kind='cubic')
# f4=interp1d(x[9::],y2,kind='cubic')
# f5=interp1d(x[9::],y3,kind='cubic')
# f6=interp1d(x[9::],y4,kind='cubic')
# x3=np.linspace(2021,2025,num=25)
# f,ax=plt.subplots()
# # plt.plot(x[10::],y[10::])
# # plt.plot(x[19::],y1,linestyle='--',color='c')
# # plt.plot(x[19::],y2,linestyle='--',color='m')
# # plt.xticks(x[10::2])
# # plt.xlabel('год')
# # plt.ylabel('цена за тонну в $')
# f2=interp1d(x,y,kind='cubic')
# x2=np.linspace(2012,2025,num=100,endpoint=True)
# x1=np.linspace(2012,2025,num=100,endpoint=True)
# ax.plot(x2,f2(x2))
# ax.plot(x1,f1(x2),color='#1E90FF')
# ax.plot(x3,f3(x3),linestyle='--',color='c')
# ax.plot(x3,f4(x3),linestyle='--',color='m')
# ax.plot(x3,f5(x3),linestyle='--',color='#40E0D0')
# ax.plot(x3,f6(x3),linestyle='--',color='#000080')
# ax.set_xticks(xnew[3::5])
# ax.set_xlabel('год')
# ax.set_ylabel('цена за тонну в $')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.grid()
# ax.legend(['цена на ЦАМ',"цена на цинк"])
# plt.show()
# f2=interp1d(x,y,kind=3)
# xnew = np.linspace(2012, 2025, num=70, endpoint=True)
# print('---')
# print(xnew)
# print(xnew,f2(xnew),'000')
# plt.plot(xnew,f2(xnew))
# plt.grid()
# plt.show()
# vals = [24, 17, 53, 21, 35]
# u=0
# for i in range(len(vals)):
#     u+=vals[i]
# print(u)
# vals=[22,47,26,5]
# names=['изготовление сплавов','цинкование','цинковые листы','прочее']
# a,ax=plt.subplots()
# ax.pie(vals,labels=names)
# plt.show()
x=[0,0.95,1,1.05,1.7,2,2.5]
y=[0,0,1,0,0,1.5,-0.3]
plt.plot(x,y)
plt.show()