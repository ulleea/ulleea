n=int(input())
k=int(input())
max= 1*(k-1)+(n-k+1)**2
a=n//k
b=n%k
min= (b)*((a+1)**2)+(k-b)*((a)**2)
print (min,max)