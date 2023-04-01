import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
#2468

N = int(input())
graph = []
max_num = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 1

for _ in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

    for j in row:
        if j > max_num:
            max_num = j

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
            if graph[nx][ny] > h:
                visited[nx][ny] = 1
                dfs(nx,ny,h)

for i in range(max_num):
    visited = [[0] * N for _ in range(N)]
    ans = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                ans += 1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result,ans)
print(result)
