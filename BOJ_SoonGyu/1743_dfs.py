import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
#1743

N,M,K = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(K):
    A,B = map(int,input().split())
    graph[A-1][B-1] = 1

def dfs(x,y):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < N and 0<= ny < M:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                ans += 1
                dfs(nx,ny)
result = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            ans = 1
            dfs(i,j)
            result = max(result,ans)

print(result)

