def lcm(x,y):
    if x > y:
        m = x
    else:
        m = y
    while(True):
        if((m % x == 0) and(m % y == 0)):
            lcm = m
            break
        m += 1
    return lcm

# import math
n=int(input())
min=n**2

for i in range(n//2,0,-1):
    cur=lcm(i,n-i)
    # cur=math.lcm(i,n-i)
    # print(cur)
    if cur<min:
        min=cur
        ans=i,n-i
print(ans[0],ans[1])
