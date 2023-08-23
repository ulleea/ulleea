def dif(d1,m1,d2,m2):
    d=d2-d1
    m=m2-m1
    return d*1440+m

n=int(input())
g=dict()
id=[]
for i in range(n):
    s=list(input().split())
    if int(s[3]) not in g:
        g[int(s[3])]=[[int(s[0]),int(s[1])*60+int(s[2]),s[4]]]
        id.append([int(s[3]),0])
    else:
        g[int(s[3])].append([int(s[0]),int(s[1])*60+int(s[2]),s[4]])
    # a=[int(s[0]),int(s[1])*60+int(s[2]),int(s[3]),s[4]]
# print(g)
# print(id)
for i in g:
    g[i].sort()
    cur=0
    for j in range(len(id)):
        if id[j][0]==i:
            cur=j
            break
    dist=0
    summ=0
    # print(cur)
    for j in range(len(g[i])):
        if g[i][j][2]=='A':
            dist=1
            summ=0
        elif g[i][j][2]=='S' or g[i][j][2]=='C':
            # summ+=dif(g[i][j-1][0],g[i][j-1][1],g[i][j][0],g[i][j][1])
            id[cur][1]+=dif(g[i][j-dist][0],g[i][j-dist][1],g[i][j][0],g[i][j][1])
            # id[cur][2]+=summ
        else:
            #g[i][j][2]=='B'
            dist+=1
            # summ += dif(g[i][j - 1][0], g[i][j - 1][1], g[i][j][0], g[i][j][1])
# print(g)
id.sort()
s=''
for i in id:
    s+=str(i[1])+' '
print(s)

