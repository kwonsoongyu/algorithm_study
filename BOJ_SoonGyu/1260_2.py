import sys
from collections import deque
#1260
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

DFS = [False] * (N+1)
BFS = [False] * (N+1)

def bfs(V):
    q = deque([V])
    BFS[V] = True
    while q:
        v= q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not BFS[i]:
                BFS[i] = True
                q.append(i)

def dfs(V):
    DFS[V] = True
    print(V,end=" ")
    for i in graph[V]:
        if not DFS[i]:
            dfs(i)

dfs(V)
print()
bfs(V)
