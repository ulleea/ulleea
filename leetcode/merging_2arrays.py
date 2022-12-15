a=[1,3,5,7]
b=[2,4,6,8,9,10]
n=len(a)
m=len(b)
# i=j=0
# c=[]
# while i<n and j<m:
#     if a[i]<b[j]:
#         c.append(a[i])
#         i+=1
#     else:
#         c.append(b[j])
#         j+=1
# if i==n:
#     c+=b[j:m]
# else:
#     c+=a[i:n]
# print(c)
#
# if (n+m)%2==1:
#     cent=(n+m)//2+1
#     nu=False
# else:
#     cent = (n + m) // 2
#     nu=True
# l=0
# l1,l2,r1,r2=0,0,n-1,m-1
# c1=n//2
# c2=m//2
# if a[c1]<b[c2]:
#     l=c1-1
# else:
#     l=c2-1
# while l!=cent-1:
#     if l<cent-1:
#
#         l=c1+c2-2
#     else:
#         l = c2 - 1
print(m,m>>2)