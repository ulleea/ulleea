s='DCXXI'
s += ' '
n = len(s)
sum = 0
a = b = c = 0
for i in range(n):
    print(s[i],sum)
    if s[i] == 'I':
        c = 1
    elif s[i] == 'V':
        c = 5
    elif s[i] == 'X':
        c = 10
    elif s[i] == 'L':
        c = 50
    elif s[i] == 'C':
        c = 100
    elif s[i] == 'D':
        c = 500
    elif s[i] == 'M':
        c = 1000
    else:
        c = 0
    print(a,b,c)
    print('---')
    if b == 0:
        b = c
    elif c == b:
        if c == a:
            sum += a + b + c
            a = b = c = 0
        else:
            a, b = b, c
    elif c != b and b != 0:
        if a == b:
            sum += a + b
            a = 0
            b=c
        elif c > b:
            sum += c - b
            b = 0
        else:
            sum += b
            b = c
    if c == 0:
        sum += a + b + c

print(sum)