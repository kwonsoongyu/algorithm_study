import sys
from collections import deque
#1325
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] * (N+1) for i in range(N+1)]
result = []

for i in range(M):
    A,B = map(int,input().split())
    graph[B].append(A)

def bfs(v):
    q = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    cnt = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]= True
                cnt += 1
    return cnt

max_value = -1

for i in range(1, N+1):
    ending = bfs(i)
    if ending > max_value:
        max_value = ending
        result.clear()
        result.append(i)
    elif ending == max_value:
        result.append(i)

for i in result:
    print(i, end= " ")
