from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
# def func(x, a,b):
#      return a*x+b
# # xdata = np.linspace(0, 4, 50)
# # y = func(xdata, 2.5, 1.3, 0.5)
# # ydata = y + 0.2 * np.random.normal(size=len(xdata))
# # plt.plot(xdata, ydata, 'b-')
# # popt, pcov = curve_fit(func, xdata, ydata)
# # y2 = [func(i, popt[0], popt[1], popt[2]) for i in xdata]
# # plt.plot(xdata, y2, 'r--')
# # print(popt)
# # print(pcov)
# # plt.grid()
# # plt.show()
#
#
# x2172=[6.225,6.218,5.762,4.781,4.225,3.644,3.067,2.548,1.556,0.889,0.452,0.001,-0.250,-1.127,-1.770]
# y2172=[0.581,0.578,0.574,0.568,0.560,0.545,0.529,0.512,0.458,0.320,0.172,0.068,0.027,-0.006,-0.005]
# sqy2172=[]
# for i in range(len(x2172)):
#     sqy2172.append(abs(y2172[i])**(1/2)*(y2172[i]/abs(y2172[i])))
# x1873=[1.100,0.820,0.420,0.150,0,-0.130,-0.748]
# y1873=[0.260,0.190,0.120,0.081,0.038,0.026,-0.015]
# sqy1873=[]
# for i in range(len(y1873)):
#     sqy1873.append(abs(y1873[i])**(1/2)*(y1873[i]/abs(y1873[i])))
# x2235=[0.643,0.416,0.251,0.178,0.081,0.04,-0.204]
# y2235=[0.247,0.184,0.118,0.102,0.083,0.070,0.038]
# sqy2235=[]
# for i in range(len(y2235)):
#     sqy2235.append(abs(y2235[i])**(1/2)*(y2235[i]/abs(y2235[i])))
# x2318=[0.767,0.554,0.363,0.080,-0.025,-0.153,-0.453]
# y2318=[0.287,0.236,0.164,0.075,0.050,0.024,0.003]
# sqy2318=[]
# for i in range(len(y2318)):
#     sqy2318.append(abs(y2318[i])**(1/2)*(y2318[i]/abs(y2318[i])))
# x2412=[0.905,0.648,0.427,0.248,-0.02,-0.244,-0.365]
# y2412=[0.369,0.281,0.193,0.151,0.054,0.028,0.004]
# sqy2412=[]
# for i in range(len(y2412)):
#     sqy2412.append(abs(y2412[i])**(1/2)*(y2412[i]/abs(y2412[i])))
#
# # print(sqy2172)
# # print(sqy1873)
# # print(sqy2235)
# # print(sqy2318)
# # print(sqy2412)
#
# # coef1,_=curve_fit(func,x2172[8:12],sqy2172[8:12])
# # arg2172=[x2172[7]*coef1[0]+coef1[1],x2172[-1]*coef1[0]+coef1[1]]
# # arg2172x=[x2172[7],x2172[-1]]
# #
# # plt.plot(arg2172x,arg2172)
# # plt.plot(x2172,sqy2172,'ro')
# # plt.title(2172)
# # plt.grid()
# # plt.show()
#
# # coef2,_=curve_fit(func,x1873,sqy1873 )
# # arg1873=[x1873[0]*coef2[0]+coef2[1],x1873[-1]*coef2[0]+coef2[1]]
# # arg1873x=[x1873[0],x1873[-1]]
# # plt.plot(arg1873x,arg1873)
# # plt.plot(x1873,sqy1873,'ro')
# # plt.title(1873)
# # plt.grid()
# # plt.show()
#
# print(x2318)
# print(sqy2318)
#
# coef3,_=curve_fit(func,x2318,sqy2318 )
# arg2318=[x2318[0]*coef3[0]+coef3[1],x2318[-1]*coef3[0]+coef3[1]]
# arg2318x=[x2318[0],x2318[-1]]
# plt.plot(arg2318x,arg2318)
# plt.plot(x2318,sqy2318,'ro')
# plt.title(2318)
# plt.grid()
# plt.show()
#
#
#
# print(x2412)
# print(sqy2412)
# coef4,_=curve_fit(func,x2412,sqy2412 )
# arg2412=[x2412[0]*coef4[0]+coef4[1],x2412[-1]*coef4[0]+coef4[1]]
# arg2412x=[x2412[0],x2412[-1]]
# plt.plot(arg2412x,arg2412)
# plt.plot(x2412,sqy2412,'ro')
# plt.title(2412)
# plt.grid()
# plt.show()
#
#
#
# coef5,_=curve_fit(func,x2235,sqy2235 )
# arg2235=[x2235[0]*coef5[0]+coef5[1],x2235[-1]*coef5[0]+coef5[1]]
# arg2235x=[x2235[0],x2235[-1]]
# plt.plot(arg2235x,arg2235)
# plt.plot(x2235,sqy2235,'ro')
# plt.title(2235)
# plt.grid()
# # plt.show()
#
# # print('coef1',coef1)
# # print('coef2',coef2)
# print('coef3',coef3)
# print('coef4',coef4)
# print('realcoef3',coef5)
#
#
#
# # x=2333
# # s=0.009638*x**2-2.636555*x+6403.78983
# # print(s,'A')
def fa(x,a,b):
    return a*x+b
x=[2.89579,3.0067,3.10175,3.16958,3.48879]
y=[0.518,0.578,0.742,0.792,0.826]
args,_=curve_fit(fa,x,y)
print(args)
plt.plot([1.8141,3.48879],[1.8141*args[0]+args[1],3.48879*args[0]+args[1]])
plt.plot(x,y,'ro')
plt.grid()
plt.show()