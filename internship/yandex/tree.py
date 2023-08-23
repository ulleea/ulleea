class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None

class Tree:

    def fill(self,n):
        self.add_root(1)
        cur=self.root
        q=2*cur.v
        w=q+1
        if q<=n:
            cur.l=Node(q)
            cur.l.p=cur
            self._fill(cur.l,n)
        if w <= n:
            cur.r = Node(w)
            cur.r.p = cur
            self._fill(cur.r, n)

    def _fill(self,cur,n):
        # print(cur.v)
        q = 2 * cur.v
        w = q + 1
        if q<=n:
            cur.l=Node(q)
            cur.l.p=cur
            self._fill(cur.l,n)
        if w <= n:
            cur.r = Node(w)
            cur.r.p = cur
            self._fill(cur.r, n)

    def add_root(self, val):
        self.root=Node(val)

    def find(self,val):
        if self.root.v==val:
            return self.root
        else:
            ans=False
            if self.root.l:
                ans=self._find(val, self.root.l)
            if self.root.r and(not ans):
                ans=self._find(val, self.root.r)
            return ans

    def _find(self,val,cur):
        if cur.v==val:
            return cur
        else:
            ans=False
            if cur.l:
                ans=self._find(val,cur.l)
            if cur.r and(not ans):
                ans=self._find(val,cur.r)
        return ans


    def swap(self,val):
        # print(val)
        node=self.find(val)
        if node==self.root:
            return
        # print(node.v)
        # print('-=-=-=-')
        prev=node.p
        gr = prev.p
        if prev==None:
            return
        if prev.p==None:
            if node == prev.l:
                node.p=None
                prev.p=node
                a=node.l
                node.l=prev
                prev.l=a
                if a:
                    a.p=prev

                # prev.p, node.l, prev.l, node.p , node.l.p =  node, prev, node.l, prev.p, prev
                self.root=node
            else:
        #         node==prev.r
                node.p = None
                prev.p = node
                a = node.r
                node.r = prev
                prev.r = a
                if a:
                    a.p = prev

                # prev.p, node.r, prev.r, node.p , node.r.p = node, prev, node.r, prev.p, prev
                self.root = node
        else:

            if node==prev.l:
                if prev.p.l==prev:
                    gr.l = node
                    prev.p = node
                    a = node.l
                    node.l = prev
                    prev.l = a
                    if a:
                        a.p = prev
                    node.p = gr
                    # prev.p.l , prev.p , node.l , prev.l,node.p, node.l.p = node , node , prev, node.l,prev.p, prev
                else:
        #             prev.p.r==prev

                    gr.r = node
                    prev.p = node
                    a = node.l
                    node.l = prev
                    prev.l = a
                    if a:
                        a.p = prev
                    node.p = gr
                    # prev.p.r , prev.p , node.l , prev.l,node.p , node.l.p= node , node , prev, node.l,prev.p,prev
            else:
                # node==prev.r
                if prev.p.l==prev:

                    gr.l=node
                    prev.p=node
                    a=node.r
                    node.r=prev
                    prev.r=a
                    if a:
                        a.p=prev
                    node.p=gr
                    # print(';;;')
                    # print(node.v,prev.v,prev.p.v,prev.p.l.v)
                    # # prev.p.l , prev.p , node.r , prev.r,node.p , node.r.p = node , node , prev, node.r,prev.p,prev
                    # print(gr.l==node)
                    # print(prev.p==node)
                    # print(node.r==prev)
                    # print()
                else:
        #             prev.p.r==prev
                    gr.r = node
                    prev.p = node
                    a = node.r
                    node.r = prev
                    prev.r = a
                    if a:
                        a.p = prev
                    node.p = gr
                    # prev.p.r , prev.p , node.r , prev.r,node.p , node.r.p = node , node , prev, node.r,prev.p,prev

    def _lvr(self,cur):
        if cur:
            # print(cur.v)
            self._lvr(cur.l)
            # print('l')
            self.s=self.s+str(cur.v)+' '
            self._lvr(cur.r)
            # print('r')

    def lvr(self):
        self.s = ''
        self._lvr(self.root.l)
        self.s=self.s+str(self.root.v)+' '
        # print(self.root.r.v)
        self._lvr(self.root.r)
        return self.s

n,q=map(int,input().split())
s=list(map(int,input().split()))
# print(s)
# n=10
tree=Tree()
tree.fill(n)
# print(tree.lvr())
# print(tree.find(10))
# print('--')
# print(s)
for i in s:
    # print(i)
    tree.swap(i)
    # print(tree.lvr())
st=tree.lvr()
print(st)

# print(tree.lvr())
# b=tree.find(5)
# print()
# tree.swap(5)
# print(tree.lvr())
# b=tree.find(5)
# print()
# print(b.r.v, b.r.l.v,b.l.v)
# print('-=-=5')
# print()
# # print(tree.lvr())
# tree.swap(4)
# print(tree.lvr())
# a=tree.find(4)
# print(a.l.v,a.r.v)
# print(a.l.p.v,a.r.p.v)
# print('-=-4')
# b=tree.find(8)
# print(b.p.v)
# tree.swap(8)



# a=tree.find(2)
# b=tree.find(4)
# c=tree.find(8)
# print(a.l,a.r,a.p.v)

