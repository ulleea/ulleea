class TrieNode:
    def __init__(self, l=None, r=None):
        self.l = l
        self.r = r
class Trie:
    def fmax(self, n):
        cur = self.head
        res = 0
        for i in range(31,-1,-1):
            if (n >> i) & 1 == 0:
                if cur.r is not None:
                    res |= 1 << i
                    cur = cur.r
                else:
                    cur = cur.l
            else:
                if cur.l is not None:
                    res |= 1 << i
                    cur = cur.l
                else:
                    cur = cur.r
        return res
    def __init__(self):
        self.head = TrieNode()
    def insert(self, n):
        cur = self.head
        for i in range(31,-1,-1):
            if (n >> i) & 1 == 0:
                if cur.l is None:
                    cur.l = TrieNode()
                cur = cur.l
            else:
                if cur.r is None:
                    cur.r = TrieNode()
                cur = cur.r

n = int(input())
vertex, max = Trie(), 0
for i in range(n):
    m = int(input())
    vertex.insert(m)
    if max<vertex.fmax(m):
        print(vertex.fmax(m))
    else:
        print(max)

