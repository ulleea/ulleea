def it(j,sum1,ansar,ans):
    for i in range(a[  set1[j]  ][0],a[  set1[j]  ][1]+1):
        sum=sum1
        sum+=i
        ansar[set1[j]]=i
        if j+1<half:
            # print(ans,sum,ansar,j)
            if sum<=s:
                cur=it(j+1,sum,ansar,ans)
            else:
                return -1
            if cur>ans:
                ans=cur
        else:
            cur=sorted(ansar)[half-1]
            if sum<=s:
                if cur>ans:
                    ans=cur
            # else:
            #     print('err',ans,cur,sum,ansar,j )
            #     return -1
        # print('>',ans,cur,sum,ansar,j)
        # print(sorted(ansar))
    return ans

import itertools
n,s=map(int,input().split())
a=[]
half=n//2+1
ind=[i for i in range(n)]
for i in range(n):
    str=input().split()
    a.append((int(str[0]), int(str[1])))
iter=itertools.combinations(ind,half-1)
# print(a)
ans=0
for i in iter:
    # print(i)
    sum=0
    set1=[]
    ansar=[0 for i in range(n)]
    for j in ind:
        if j in i:
            sum+=a[j][0]
            ansar[j]=a[j][0]
        else:
            set1.append(j)
    # print('====',set1,sum)
    cur=it(0,sum,ansar,0)
    # print('---',ans,cur)
    if cur>ans:
        ans=cur

print(ans)