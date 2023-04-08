import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#1245

N,M = map(int,input().split())
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
graph = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    global trigger
    visited[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < N and 0<= ny < M:
            if graph[x][y] < graph[nx][ny]:
                trigger = False
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                dfs(nx,ny)
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and visited[i][j] == 0:
            trigger = True
            dfs(i,j)

            if trigger == True:
                result += 1

print(result)
