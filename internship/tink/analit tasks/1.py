n=6
t=1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if j>i and k>j:
                print(t,(i,j,k))
                t+=1