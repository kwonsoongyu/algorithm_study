import sys
from collections import deque
#1260
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[0]*(N+1) for i in range(N+1)]


for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS = [0]*(N+1) #dfs 방문기록
BFS = [0]*(N+1) #bfs 방문기록

def bfs(v):
    q = deque([v])
    BFS[v] = 1
    while q:
        v = q.popleft()
        print(v,end=" ")
        for i in range(1, N+1):
            if not BFS[i] and graph[v][i]:
                q.append(i)
                BFS[i] = 1

def dfs(v):
    DFS[v] = 1
    print(v, end = " ")
    for i in range(1, N+1):
        if not DFS[i] and graph[v][i]:
            dfs(i)
dfs(V)
print()
bfs(V)
