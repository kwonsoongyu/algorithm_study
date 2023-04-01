import sys
input = sys.stdin.readline
from collections import deque
#2468

N = int(input())
graph = []
max_num = 0
result = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

    for j in row:
        if max_num < j:
            max_num = j

def bfs(x,y,h):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N and graph[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx,ny])

for i in range(max_num):
    ans = 0
    visited = [[0]*N for _ in range(N)]

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                ans += 1
                bfs(j,k,i)
    result = max(result,ans)

print(result)
