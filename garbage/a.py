n=int(input())
left=[]
right=[]
for i in range(n):
    s=input().split()
    left.append(int(s[0]))
    right.append(int(s[1]))
left.sort(reverse=True)
right.sort(reverse=True)
# print(left)
# print(right)
lcount=0
last=0
total=0
# for i in range(2*n):
i=0
while len(left)>0 and len(right)>0:
    if left[-1] >= right[-1]:
        # print('>')
        x=right.pop()
        if lcount == 1:
            total+=x-last
        lcount-=1
        if lcount==1:
            last=x

    elif left[-1]<right[-1]:
        x=left.pop()
        lcount+=1
        if lcount==2:
            total+=x-last
        elif lcount==1:
            last=x
    # print(x,lcount,last)
while len(right)>0:
    x=right.pop()
    if lcount==1:
        total+=x-last
    lcount-=1
    if lcount==1:
        last=x

print(total)