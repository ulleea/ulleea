n=int(input())
# n=0
ans=[]
for i in range(n):
    s=input().split(',')
    s[3]=int(s[3])
    s[4]=int(s[4])
    st=set()
    for j in s[0]:
        st.add(j)
    for j in s[1]:
        st.add(j)
    for j in s[2]:
        st.add(j)
    sm=0
    x=s[4]
    while x>0:
        a=x%10
        sm+=a
        x//=10
    x = s[3]
    while x > 0:
        a = x % 10
        sm += a
        x //= 10
    sm=sm<<6
    numb=(ord(s[0][0].lower())-ord('a')+1)<<8
    summ=numb+sm+len(st)
    summ=format(summ, 'X')
    summ='000'+summ
    a=''
    m=len(summ)
    for j in range(m-1,m-4,-1):
        a=summ[j]+a
    ans.append(a)
    # print(a)
print(' '.join(ans))

