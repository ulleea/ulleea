n,m,k=map(int,input().split())
x=1 if (n*k)%m!=0 else 0
print((n*k)//m+x)