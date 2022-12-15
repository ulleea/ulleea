import time
base = 13
q = 1000003
const=ord('a') - 1
def code(ch):
    return ord(ch) - const

def polynomial_hash(s):
    hash = 0
    ser=set()
    for char in s:
        ser.add(char)
        hash = (hash * base + code(char)) % q
    return hash,len(ser)

def next_hash(hash, first_ch, new_ch, base_powered,k):
    if k==1 and first_ch==new_ch:
        return hash
    global base, q
    return ((hash - code(first_ch) * base_powered) * base + code(new_ch)) % q

def RK(s, sub, base_powered):
    h,k = polynomial_hash(sub)
    n = len(s)
    m = len(sub)
    occurrences = []
    h1,p = polynomial_hash(s[:m])
    if h == h1:
        occurrences.append(0)
    for i in range(n-m):
        h1 = next_hash(h1, s[i], s[i+m], base_powered,k)
        if h == h1:
            occurrences.append(i+1)
    return occurrences

def fast_pow(x, y):
    if y == 0:
        return 1
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p

def _main():
    A = input()
    B = input()
    occurrences = RK(B, A, base**(len(A)-1))
    if occurrences:
        print(' '.join(map(str, occurrences)))
    else:
        print(-1)

_main()