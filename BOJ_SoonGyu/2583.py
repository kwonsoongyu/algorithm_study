import sys
from collections import deque
input = sys.stdin.readline
#2583

M,N,K = map(int,input().split())
graph = [[0]*N for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    for j in range(y1,y2):
        for t in range(x1,x2):
            graph[j][t] = 1

result = []
q = deque()

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 1
            q.append([i,j])
            graph[i][j] = 1
            while q:
                x,y = q.popleft()

                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]

                    if 0<= nx < M and 0<= ny < N and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        count += 1
                        q.append([nx,ny])
            result.append(count)

print(len(result))
result.sort()
print(*result)

