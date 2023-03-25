import sys
from collections import deque
#7566
input = sys.stdin.readline


M,N = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
flag = True
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < M and 0<= ny < N and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny,nx))


bfs()
maxday = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = False
        if graph[i][j] > maxday:
            maxday = graph[i][j]
if flag == True:
    print(maxday-1)
else:
    print(-1)
