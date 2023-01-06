import sys
from collections import deque
#2178
input = sys.stdin.readline

M,N = map(int,input().split())

graph = []

for i in range(M):
    graph.append(list(map(int,input().rstrip())))

def bfs(x,y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x,y))
    while q:
        x, y = q[0][0],q[0][1]
        q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1

    return graph[M-1][N-1]

print(bfs(0,0))
