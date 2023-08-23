n=int(input())
s=input()
a=[-1 for i in range(4)]
minc=len(s)+1
A=B=C=D=0
for i in range(n):
    if s[i]=='a':
        a[0]=i
        A=1
    elif s[i]=='b':
        a[1]=i
        B=1
    elif s[i]=='c':
        a[2]=i
        C=1
    elif s[i]=='d':
        a[3]=i
        D=1
    if A and B and C and D:
        c=max(a)-min(a)+1
        if c<minc:
            minc=c
if not (A and B and C and D):
    print(-1)
else:
    print(minc)