def area(i,j):
    if i<0 and j<0:
        # print('---')
        return 0
    i+=1
    j+=1
    x1=r*cos(c*i)
    x2=r*cos(c*(i+j))
    y1 = r * sin(c * i)
    y2 = r * sin(c * (i + j))
    l0=((x1-x0)**2+(y1-y0)**2)**(1/2)
    l1=((x2-x1)**2+(y2-y1)**2)**(1/2)
    l2=((x2-x0)**2+(y2-y0)**2)**(1/2)
    p=(l0+l1+l2)/2
    s=(p*(p-l0)*(p-l1)*(p-l2))**(1/2)
    return s

def tr(n,g):
    j,k=n-1,(n-1)//2
    # print(n,(k,j))
    if (k-1,j-k-1) not in g:
        g[(k-1,j-k-1)]=1
    else:
        g[(k-1,j-k-1)]+=1
    if k>2:
        tr(k-1,g)
    if j-k>2:
        tr(j-k-1,g)

from math import *
n=int(input())
# start=time.time()
r,c=1/(2*sin(pi/n)),  2*pi/n
x0,y0=r,0
x,y,z=0,round(n/3),2*round(n/3)
# print(x,y,z)
# # print(area())
# print(y-x-1,z-y-1,n-z-1)
g=dict()

# if y-x-1==n-z-1:
#     if y-x-1>2:
#         tr(y-x-1,g)
#         for i in g:
#             g[i]*=3
# else:
#     if y - x - 1 > 2:
#         tr(y-x-1,g)
#         for i in g:
#             g[i]*=2
#     if n-1-z>2:
#         tr(n-z-1,g)
tr(y-x-1,g)
tr(z-y-1,g)
tr(n-z-1,g)
s=area(round(n/3)-1,round(n/3)-1)
# while n>0:
#     x=a[0]
#     m=n-1
#     count=0
#     while m>0:
#         if x==a[m]:
#             a.pop(m)
#             count+=1
#             n-=1
#         m-=1
#     s+=count*area(x[0],x[1])

for i in g.keys():
    s+=g[i]*area(i[0],i[1])

print(s)
# print(time.time()-start)
