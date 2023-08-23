n=int(input())
a=list(map(int,input().split()))
g=dict()
g[1]=set()
g[2]=set()
max=3
uniq=set()
ans=0
l=0
for i in a:
    l+=1
    uniq.add(i)
    n=len(uniq)
    ind=0
    for j in range(1,max):
        if i in g[j]:
            g[j].remove(i)
            if j+1 in g:
                g[j+1].add(i)
                ind=1
                break
            else:
                g[j+1]={i}
                max+=1
                ind=1
                break
    # print('==')
    if not ind:
        g[1].add(i)
        ind=1
    # print(ans,l,g)
    for j in g.keys():
        if len(g[j])==n or len(g[j])==n-1 and l>ans:
            ans=l
print(ans)