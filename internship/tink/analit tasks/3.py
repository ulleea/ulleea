a=[]
n=1025
for i in range(1,n):
    a.append(i)
print(a)
for j in range(1,11):
    print(j,a)
    if j %2==1:
        i=0
        while i<len(a):
            a.pop(i)
            i+=1
    else:
        i=1
        while i<len(a):
            a.pop(i)
            i+=1
print(a)