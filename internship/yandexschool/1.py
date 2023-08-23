def getmin(r, n):
    min = 1
    minv = r[1][0]*r[1][1]
    for i in range(2,n+1):
        if r[i][1]*r[i][0] < minv:
            minv = r[i][1]*r[i][0]
            min = i
    return min

def getmax(r, n):
    max = 1
    maxv = r[1][0]*r[1][1]
    for i in range(2,n+1):
        if r[i][1]*r[i][0] > maxv:
            maxv = r[i][1]*r[i][0]
            max = i
    return max


n, m, q = map(int,input().split())
r = [[0, m] for i in range(n+1)]
min = 1
max = 1
# print(r)
for i in range(q):
    s = input().split()
    k = len(s)
    if k == 3:
        s1=int(s[1])
        r[s1][1] -= 1
        if s1 != min and s1 != max:
            min = getmin(r, n)
        elif s1 != min and s1 == max:
            min = getmin(r,n)
            max = getmax(r, n)
        elif s1 == min and s1 != max:
            pass
        else:
            min = getmin(r, n)
            max = getmax(r, n)

    elif k == 2:
        s1 = int(s[1])
        r[s1][0] += 1
        r[s1][1] = m
        if s1 != min and s1 != max:
            max = getmax(r, n)
        elif s1 != min and s1 == max:
            pass
        elif s1 == min and s1 != max:
            min = getmin(r, n)
            max = getmax(r, n)
        else:
            min = getmin(r, n)
            max = getmax(r, n)

    elif k == 1:
        if s == ['GETMIN']:
            print(min)
        else:
            print(max)
        # print(s,r[1:],min,max)
