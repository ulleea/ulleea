import matplotlib.pyplot as plt
import math

y1=[26.17,23.56,9.11,6.89,9.46,7.9,6.77,5.91,5.57,4.96,4.38,4,4.17,3.75,3.33,3.26,3.16,2.78,2.58,2.55,2.82,2.28,2.24,2.13,2,1.92,1.97,1.83]
x1=[]
#
c=y1[0]
for i in range(1,29):
    y1[i-1]/=c
    x1.append(i)
# print(y1)
plt.plot(x1,y1)
plt.grid()
plt.show()

y2=[]
x2=[]
with open('F:\python\project\\paraprog.txt','r') as file:
    for line in file:
        # print(line)
        s=line
        s=s.split()
        # print(s)
        y2.append(float(s[2]))
print(y2)
c=y2[0]
for i in range(28):
    y2[i]/=c
print(y2)
# print(x1)
# print(len(y2),len(x1))
# # print(len(y2))
plt.plot(x1,y2)
plt.grid()
plt.show()
y3=[0.0211097, 0.0106776, 0.00716739, 0.005529]
c=y3[0]
for i in range(4):
    y3[i]/=c
x3=[1,2,3,4]
plt.plot(x3,y3)
plt.grid()
plt.show()
y4=[0.00212528,0.00106912,0.00071974,0.000530957]
c=y4[0]
for i in range(4):
    y4[i]/=c
x4=[1,2,3,4]
plt.plot(x4,y4)
plt.grid()
plt.show()
y5=[95,72,55,42]
c=y5[0]
for i in range(4):
    y5[i]/=c
plt.plot(x3,y5)
plt.grid()
plt.show()
y6=[237,158,115,92]
c=y6[0]
for i in range(4):
    y6[i]/=c
plt.plot(x3,y6)
plt.grid()
plt.show()