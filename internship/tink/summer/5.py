def count(begin,l,r):
    if begin<=l:
        return l+1,(l-begin+1)*(n-r)
    else:
        return begin,0

n=int(input())
a=list(map(int,input().split()))
g=dict()
sum=0
# ans=[]
total=0
begin=0
for i in range(n):
    sum+=a[i]
    if sum in g.keys():
        # print(sum,ans,g[sum])
        # ans.append([g[sum]+1,i])
        begin,add=count(begin,g[sum]+1,i)
        total+=add
        g[sum]=i
    else:
        g[sum]=i
        if sum==0:
            # ans.append([0,i])
            begin,add=count(begin,0,i)
            total+=add
    # print(ans,g,total)
print(total)