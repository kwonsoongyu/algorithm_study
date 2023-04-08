import sys
input = sys.stdin.readline
from collections import deque
#1245

N,M = map(int,input().split())
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
graph = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    global result
    trigger = True
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx < N and 0<= ny < M:
                if graph[nx][ny] == graph[a][b]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                elif graph[nx][ny] > graph[a][b]:
                    trigger = False
    if trigger:
        result += 1

result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i,j)

print(result)
