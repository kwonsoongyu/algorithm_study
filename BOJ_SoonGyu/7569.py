import sys
from collections import deque
#7569
input = sys.stdin.readline

M,N,H = map(int,input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z,x,y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nz<H and 0<=nx<N and 0<= ny < M:
                if graph[nz][nx][ny] == 0:
                    q.append((nz,nx,ny))
                    graph[nz][nx][ny] = graph[z][x][y] + 1



for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                q.append((z,x,y))

bfs()

flag = 0
result = -2
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                flag = 1
            result = max(result,graph[i][j][k])

if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)


