course=list(map(int,input().split()))
wallet=list(map(int,input().split()))
for i in range(3):
    # wallet[i]-=wallet[i]%course[i]
    wallet[i]=wallet[i]//course[i]
# print(wallet)
# print(course)
n=sum(wallet)
comb=int((n+2)*(n+1)/2)
print(comb)