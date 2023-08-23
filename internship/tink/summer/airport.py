# def dijkstra(g):
# #     visited={}
# #     w=[n+1 for i in range(n)]
# #     w[0]=0
# #     while
# #     return
#     from collections import deque
#     # N, M, start_v, end_v = map(int, input().split())
#
#     # G = {i: set() for i in range(N)}
#     #
#     # for _ in range(M):
#     #     v1, v2 = map(int, input().split())
#     #     G[v1].add(v2)
#     #     G[v2].add(v1)
#     start=1
#     distances = [None] * (n+1)
#     print(distances)
#     distances[start] = 0
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         for ui in g[v]:
#             u=ui[0]
#             if distances[u] is None:
#                 distances[u] = distances[v] + 1
#                 q.append(u)
#             # else:
#             #     distances[u]=min(distances[v] + 1,distances[u])
#     print(distances)
def dfs(v, g, color, ans):
    color[v] = 1
    for u,p in g[v]:
        # u=ui[0]
        if color[u] == 0:
            dfs(u, g, color, ans)
        elif color[u] == 1:
            exit()
    color[v] = 2
    ans.append(v)

# g=dict()
n,m=map(int,input().split())
# print(n,m)
# print(s)
# for i in range(m):
#     s=list(map(int,input().split()))
#     if s[0] in g:
#         k=0
#         for j in g[s[0]]:
#             if s[1]==j[0]:
#                 j[1].add(s[2])
#                 k=1
#         if k==0:
#             g[s[0]].append([s[1],{s[2]}])
#     else:
#         g[s[0]]=[[s[1],{s[2]}]]
# print(g)
from collections import deque
# start_v, end_v = 1, n

g = {i: set() for i in range(1,n+1)}
for _ in range(m):
    v1, v2, p = map(int, input().split())
    g[v1 ].add((v2 , p))
# print(g)
color = [0] * (n+1)
ans = []
for v in g:
    # print(v)
    if color[v] == 0:
        dfs(v, g, color, ans)
ans=ans[::-1]
s=''
print(ans)