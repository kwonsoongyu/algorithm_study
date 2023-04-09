import sys
input = sys.stdin.readline
from collections import deque
#1240

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A,B,distance = map(int,input().split())
    graph[A].append([B,distance])
    graph[B].append([A,distance])

def bfs(V,target):
    q = deque()
    q.append([V,0])
    BFS = [False] * (N + 1)
    BFS[V] = True
    while q:
        v,d= q.popleft()

        if v == target:
            return d
        for i,distance in graph[v]:
            if not BFS[i]:
                BFS[i] = True
                q.append([i,distance+d])



for _ in range(M):
    A,B = map(int,input().split())
    cnt = bfs(A,B)
    print(cnt)
