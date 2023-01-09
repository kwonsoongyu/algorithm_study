import sys
from collections import deque
#11724
input = sys.stdin.readline

N,M = map(int,input().split())
result = 0
graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

BFS = [0] * (N+1)

def bfs(v):
    q = deque([v])
    BFS[v] = 1
    while q:
        v = q.popleft()
        for i in range(N+1):
            if not BFS[i] and graph[v][i]:
                q.append(i)
                BFS[i] = 1

for i in range(1, N+1): #방문하지 않았다면 bfs를 돌리고 개수 증가
    if not BFS[i]:
        bfs(i)
        result += 1

print(result)
