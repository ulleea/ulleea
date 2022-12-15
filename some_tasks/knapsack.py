import time
import matplotlib.pyplot as plt

def merge_sort1(A):
    if len(A) == 1 or len(A) == 0:
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [[0]  for i in range((len(L) + len(R)))]
    while n < len(L) and m < len(R):
        if L[n][1] > R[m][1]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]; n += 1; k += 1
    while m < len(R):
        C[k] = R[m]; m += 1; k += 1
    for i in range(len(A)):
        A[i] = C[i]
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [[0]  for i in range((len(L) + len(R)))]
    while n < len(L) and m < len(R):
        if L[n][2] > R[m][2]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]; n += 1; k += 1
    while m < len(R):
        C[k] = R[m]; m += 1; k += 1
    for i in range(len(A)):
        A[i] = C[i]

def func(cw,n,cv,total_weight,p,a,c):
    global max,weight
    if n+1<len(a) and cv+c[n+1]>total_max:
    # if n + 1 < len(a):
        func(cw,n+1,cv,total_weight,p,a,c)
    else:
        if cv>max:
            max=cv
            weight=cw
    if n+1< len(a) and cw+a[n][0]<=total_weight and cv+c[n+1]>total_max:
    # if n + 1 < len(a) and cw+a[n][0]<=total_weight:
        func(cw+a[n][0],n+1,cv+a[n][1],total_weight,p,a,c)
    else:
        if cv>max:
            max=cv
            weight=cw
def summs(c,a,w,n):
    sum=0
    sumv=0
    num=int(n/4)
    for i in range(n-1,-1,-1):
        # sum+=a[i][0]
        sumv+=a[i][1]
        # c[i][0]=sum
        c[i]=sumv
    sum=0
    max=0
    for i in range(n-1,-1,-1):
        if max+a[i][0]<=w:
            sum+=a[i][1]
            max+=a[i][0]
    total_max=sum
    for _ in range(num):
        sum=0
        max=0
        for i in range(_):
            if max + a[i][0] <= w:
                sum += a[i][1]
                max += a[i][0]
        for j in range(n-1,_,-1):
            if max + a[j][0] <= w:
                sum += a[j][1]
                max += a[j][0]
        if sum > total_max:
            total_max = sum
    return c,total_max
w=int(input())
n=int(input())
t=time.time()
a=[]
# b=[]
max=0
for i in range(n):
    s=input().split()
    s=[int(s[0]),int(s[1])]
    if s[0]<w:
        s.append(s[1]/s[0])
        a.append(s)
        # b.append(s)
n=len(a)
# for i in range(n):
#     for j in range(n):
#         # if a[j][2]<a[i][2]:
#         #     a[j],a[i]=a[i],a[j]
#         if b[j][2]<b[i][2]:
#             b[j],b[i]=b[i],b[j]
merge_sort1(a)
# print(a)
# print(b)
# c,total_max=summs([[0,0] for i in range(n)],a,w,n)
c,total_max=summs([0 for i in range(n)],a,w,n)
merge_sort(a)
c,v=summs([0 for i in range(n)],a,w,n)
if v> total_max:
    total_max=v
# print(c)
p=[]
max=0
weight=0
func(0,0,0,w,p,a,c)
t=time.time()-t
print(max)