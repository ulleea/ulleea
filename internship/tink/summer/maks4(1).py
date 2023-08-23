from math import *
from time import time


triangles = {}

def area(n, i, j):
    r, c = 1/(2*sin(pi/n)), 2*pi/n
    x0, y0 = r, 0
    x1 = r*cos(c*i)
    x2 = r*cos(c*(i+j))
    y1 = r * sin(c * i)
    y2 = r * sin(c * (i + j))
    l0 = ((x1-x0)**2+(y1-y0)**2)**(1/2)
    l1 = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    l2 = ((x2-x0)**2+(y2-y0)**2)**(1/2)
    p = (l0+l1+l2)/2
    return (p*(p-l0)*(p-l1)*(p-l2))**(1/2)


def main(n):
    v = (0, round(n/3), 2*round(n/3))
    s = area(n, v[1]-v[0], v[2]-v[1])
    
    subtriangle(1, v[1]-1)
    subtriangle(v[1]+1, v[2]-1)
    subtriangle(v[2]+1, n-1)

    for key in triangles:
        s += area(n, key[0], key[1]) * triangles[key]
    return s

def subtriangle(v0, v2):
    if v0 + 1 >= v2:
        return True

    v1 = (v2 + v0) // 2
    diffs = (v1-v0, v2-v1)
    if diffs not in triangles:
        triangles[diffs] = 1
    else:
        triangles[diffs] += 1
    
    subtriangle(v0+1, v1-1)
    subtriangle(v1+1, v2-1)


if __name__ == "__main__":
    n = int(input())
    start = time()
    print(main(n))
    print(time() - start)
