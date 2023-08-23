n,x=map(int,input().split())
a=list(map(int,input().split()))
pref=[0 for i in range(n)]
sum=0
ind=0
for i in range(n):
    if a[i]==x:
        ind=1
        break
    sum+=a[i]*(-1)**(i%2)
    if sum==x:
        ind=1
        break
    pref[i]=sum
# print(pref)
for i in range(1,n):
    for j in range(1,n-i):
        if (pref[i+j-1]-pref[i-1])*(-1)**(i%2)==x:
            ind=1
            break
if not ind:
    print('NO')
else:
    print('YES')