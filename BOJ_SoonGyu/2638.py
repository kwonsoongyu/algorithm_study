import sys
input = sys.stdin.readline
from collections import deque
#2638

N,M = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
time = 0
for i in range(N):
    graph.append(list(map(int,input().split())))

def outSide():
    q = deque()
    q.append([0,0])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    graph[0][0] = -1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue
            if graph[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            q.append([nx, ny])
            visited[nx][ny] = 1
            graph[nx][ny] = -1

def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return False
    return True

while not check():
    outSide()
    result = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                count = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 > nx or nx >= N or 0 > ny or ny >= M:
                        continue
                    if graph[nx][ny] == -1:
                        count += 1

                if count >= 2:
                    result.append([i,j])

    for y,x in result:
        graph[y][x] = 0
    time += 1
print(time)

