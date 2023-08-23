words=["word","good","best","good"]
s="wordgoodgoodgoodbestword"
n=len(words)*len(words[0])
lg=len(words[0])
g=dict()
for i in words:
    if g.get(i)!=None:
        g[i][0]+=1
    else:
        g[i]=[1,0]
start=[]
i=j=0
while len(s)-i>=n:
    print('--------')
    str=s[i+j*lg : i+(j+1)*lg]
    j+=1
    print(str, i, j)
    if str in g:
        g[str][1]+=1
        print(str,g[str])
        if j==len(words):
            ind=1
            for key in g.keys():
                print(g[key][0],g[key][1],ind,'-=')
                if g[key][0]!=g[key][1]:
                    ind=0
                    break
            if ind==1:
                start.append(i)
                i+=1
                j=0
                for k in g.keys():
                    g[k][1]=0
            else:
                i+=1
                j=0
                for k in g.keys():
                    g[k][1]=0
        else:
            if g[str][0]>=g[str][1]:
                pass
            else:
                # print('g[str][0]<=g[str][1]')
                i+=1
                j=0
                for k in g.keys():
                    g[k][1]=0
    else:
        i+=1
        j=0
        for k in g.keys():
            g[k][1]=0
print(start)