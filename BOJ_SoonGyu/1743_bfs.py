import sys
input = sys.stdin.readline
from collections import deque
#1743

N,M,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(K):
    A,B = map(int,input().split())
    graph[A-1][B-1] = 1

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    max_num = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<=ny <M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    max_num += 1
    return max_num
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            part_result = bfs(i,j)
            result = max(part_result,result)
print(result)
