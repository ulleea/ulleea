n=6
t=1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if j>i and k>j:
                print(t,(i,j,k))
                t+=1
# a=[]
# n=1025
# for i in range(1,n):
#     a.append(i)
# print(a)
# for j in range(1,11):
#     print(j,a)
#     if j %2==1:
#         i=0
#         while i<len(a):
#             a.pop(i)
#             i+=1
#     else:
#         i=1
#         while i<len(a):
#             a.pop(i)
#             i+=1
# print(a)
for j in range(11,20):
    print(j%5,j%6,j)