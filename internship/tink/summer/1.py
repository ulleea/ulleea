a=list(map(int,input().split()))
inc=desc=True
for i in range(len(a)-1):
    if inc:
        if a[i]>a[i+1]:
            inc = False
    if desc:
        if a[i]<a[i+1]:
            desc=False
if inc or desc:
    print('YES')
else:
    print('NO')
