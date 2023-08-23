n=int(input())
a=list(map(int,input().split()))
g=dict()
sum=0
ans=0
for i in range(n):
    sum+=a[i]
    if sum in g.keys():
        print(sum,ans,g[sum])
        ans+=len(g[sum])
        g[sum].append(i)
        if sum==0:
            ans+=1
    else:
        g[sum]=[i]
        if sum==0:
            ans+=1
    print(ans,g)
print(ans)