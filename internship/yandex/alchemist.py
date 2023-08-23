def dfs(graph, start, cur,numb,colors=None):
    if not colors:
        colors=[0 for i in range(n+1)]
    # if visited is None:
    #     visited = set()
    # visited.add(start)
    colors[start]+=numb
    # print(start)
    # print(start,numb)
    for next in graph[start]:
        if colors[cur]<3:
            colors=dfs(graph, next[0],cur,next[1],colors)
    return colors

def counter(graph, start, cur,numb):
    a=0
    b=0
    # print(start,numb)
    if start==1:
        a+=numb
        # print('c',a,b)
        return a,b
    elif start==2:
        b+=numb
        # print('b',a,b)
        return a,b
    else:
        for next in graph[start]:
            if next[0] not in block:
                x,y=counter(graph,next[0],cur,next[1])
                a+=x*numb
                b+=y*numb
                # print(start,'v',a,b)
        return a,b



n=int(input())
g=dict()
g[1]=[]
g[2]=[]
for i in range(3,n+1):
    # print(i)
    s=list(map(int,input().split()))
    # if i not in g:
    #     g[i]=[]
    prev=0
    count=0
    ans=[]
    for j in range(1,len(s)):
        find=0
        # print(s[j],ans)
        for k in ans:
            if k[0]==s[j]:
                # print(k[0])
                k[1]+=1
                find=1
                break
        if not find:
            # print('ans')
            ans.append([s[j],1])
    g[i]=ans
# print(g)
block=set()
for i in range(3,n+1):
    a=dfs(g,i,i,1)
    # print(i)
    if a[i]>2:
        block.add(i)


# j=5
# a=dfs(g,j,j,1)
# print(a[1:3])
# print(a)
# print(block)
q=int(input())
st=''
j=5
a,b=counter(g,j,j,1)
# print(';;;')
# print(a,b)

for i in range(q):
    s=list(map(int,input().split()))
    if s[2] in block:
        st+='0'
    else:
        a,b=counter(g,s[2],s[2],1)
        # print(a,b)
        if a>s[0] or b>s[1]:
            st+='0'
        else:
            st+='1'
print(st)
