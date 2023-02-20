import sys
from collections import deque
#1926
input = sys.stdin.readline

N,M = map(int,input().split())
BFS = []
count = 0
graph = []
max = 0
for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

def bfs(x,y):
    global count
    domain = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count += 1
    q=deque()
    q.append((x,y))
    graph[x][y] = 0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0
                domain += 1
    return domain

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            num = bfs(i,j)
            if num > max:
                max = num
print(count)
print(max)
