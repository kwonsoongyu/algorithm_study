import sys
from collections import deque

# 1389
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

result = [0] * N


def bfs(v):
    q = deque([v])
    num = [0] * (N+1)
    BFS = [0] * (N + 1)
    BFS[v] = 1
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if not BFS[i] and graph[v][i]:
                q.append(i)
                BFS[i] = 1
                num[i] = num[v] + 1
    return sum(num)

for i in range(1,N+1):
    result[i-1] = bfs(i)

resultnum = min(result)
print(result.index(resultnum)+1)
