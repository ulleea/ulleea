def dfs(g,v,k,x):
    global a
    for i in g[v][1]:
        if g[v][0]-g[i][0]<=k:
            a[i]+=x
            if g[v][0]-g[i][0]<k:
                dfs(g,i,k,x)
n=int(input())
g=dict()
for i in range(1,n+1):
    g[i]=[0,set()]
g[1][0]=7
for i in range(1,n):
    a,b=map(int,input().split())
    g[a][1].add(b)
    g[b][0]=g[a][0]-1
# print(g)
q=int(input())
a=[0 for i in range(n+1)]
for i in range(q):
    v,k,x=map(int,input().split())
    a[v] += x
    dfs(g,v,k,x)
# print(a[1::])
print(' '.join(map(str,a[1::])))

