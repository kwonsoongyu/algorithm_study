import sys
from collections import deque
#14716
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
result = 0
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
graph = [list(map(int, input().split())) for i in range(N)]

def bfs(y,x):
    graph[y][x]=0
    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if (0 <= ny < N) and (0<= nx < M) and graph[ny][nx]==1:
                graph[ny][nx] = 0
                q.append((ny,nx))

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            bfs(i,j)
            result += 1

print(result)
