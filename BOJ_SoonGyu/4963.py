import sys
from collections import deque
#4963
input = sys.stdin.readline

def bfs(x,y):
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,-1,-1,1,1]

    q=deque()
    q.append((x,y))

    while q:
        x,y=q[0][0],q[0][1]
        q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < M and 0<= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

while True:
    N,M = map(int,input().split())
    result = 0
    graph = []

    if N == 0 and M == 0:
        break

    for i in range(M):
        graph.append(list(map(int,input().split())))

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i,j)
                result += 1
    print(result)

