n=int(input())
events=[]
for i in range(n):
    s=list(map(int,input().split()))
    events.append((s[0],-1,s[2],s[1]-s[0]))
    events.append((s[1],1,s[2], s[1]-s[0]))
q=int(input())
for i in range(q):
    s = list(map(int, input().split()))
    # if s[2]==1:
    #     events.append((s[0], -2, -1))
    #     events.append((s[1], 2, -1))
    # else:
    #     events.append((s[0], -2, 0))
    #     events.append((s[1], 2, 0))
    events.append((s[0], -2, s[2]-2,i))
    events.append((s[1], 2, s[2]-2,i))

events.sort()
# print(events)
counts=[]
for i in range(len(events)):
    if events[i][1]<-1:#запрос начало
        counts.append( [True, events[i][3],events[i][2],0] )
    elif events[i][1]>1:#запрос конец
        counts[events[i][3]][0]=False
    elif events[i][1]==-1:#проц начало
        for j in counts:
            if j[0] and j[2]==-1:#открытый запрос1 типа
                j[3]+=events[i][2]
            # elif j[0] and j[2]==0:
            #     j[4].append( (events[i][0],events[i][3]) )
    elif events[i][1]==1:#проц конец
        for j in counts:
            if j[0] and j[2]==0:#открытый запрос2 типа
                j[3]+=events[i][3]

# print(counts)
s=''
for i in counts:
    s+=str(i[3])+' '
print(s)