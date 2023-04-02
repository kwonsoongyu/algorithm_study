import sys
input = sys.stdin.readline
from collections import deque
#3184

R,C = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[0]*C for _ in range(R)]
sheep = 0
wolf = 0
for _ in range(R):
    row = list(input().strip())
    graph.append(row)

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    global sheep,wolf
    part_sheep = 0
    part_wolf = 0
    if graph[x][y] == 'o':
        part_sheep += 1
    if graph[x][y] == 'v':
        part_wolf += 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < R and 0<= ny < C and visited[nx][ny] == 0 and graph[nx][ny] != '#':
                if graph[nx][ny] == 'o':
                    part_sheep += 1
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 'v':
                    part_wolf += 1
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                else:
                    q.append([nx,ny])
                    visited[nx][ny] = 1

    if part_sheep > part_wolf:
            sheep += part_sheep
    else:
            wolf += part_wolf

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j] == 0:
            bfs(i,j)

print(sheep,wolf)
