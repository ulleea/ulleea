def pr(i, j):
    m = 1
    a[i][j] += 100
    a[i - 1][j - 1] = 1
    a[i][j - 1] = 1
    a[i + 1][j - 1] = 1
    a[i - 1][j] = 1
    a[i - 1][j + 1] = 1
    while 1:
        a[i + 1][j - 1] = 1
        a[i + 1][j + 1] = 1
        if a[i+1][j] == 100:
            m += 1
            i += 1
            a[i-1][j+1] = 1
            a[i][j] += 100
        else:
            a[i+1][j] = 1
            break
    if m == 1:
        while 1:
            a[i - 1][j + 1] = 1
            a[i + 1][j + 1] = 1
            if a[i][j+1] == 100:
                m += 1
                j += 1
                a[i][j] += 100
            else:
                a[i][j+1] = 1
                break
    d[m] += 1
    # print(i,j)
    # print(d)
def pr2(i, j):
    global variants,l
    m = 1
    x = i
    y = j
    while 1:
        if i+1<10 and a[i + 1][j] == 0:
            m += 1
            i += 1
        else:
            break
        if m == l:
            variants += 1
            break
    m = 1
    i = x
    j = y
    while 1:
        if j+1<10 and a[i][j+1] == 0:
            m += 1
            j += 1
        else:
            break
        if m == l:
            variants += 1
            break

a = [[0]*10 for _ in range(10)]
variants = 0
#d=dict()
#for i in range(4):

d = {1: 0, 2: 0, 3: 0, 4: 0}
for _ in range(10):
    s = input()
    for  i, j in enumerate(s):
        if j != '.':
            a[_][i] = 100
for i in range(1, 10):
    for j in range(1,10):
        if a[i][j] == 100:
            #print(i,j,'--')
            pr(i, j)
l = 0
while 1:
    if d[1] != 4:
        l = 1
        #print(l)
        break
    if d[2] != 3:
        l = 2
        #print(l)
        break
    if d[3] != 2:
        l = 3
        #print(l)
        break
    if d[4] != 1:
        l = 4
        #print(l)
        break

if l == 1:
    for i in range(1, 10):
        for j in range(1, 10):
            if a[i][j] == 0:
                variants += 1
else:
    for i in range(1, 10):
        for j in range(1,10):
            if a[i][j] == 0:
                pr2(i, j)
#print(a)
print(variants)