import sys
from collections import deque
#1012
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    global result
    q.append([x,y])
    graph[x][y]=0

    while q:
        a,b = q.popleft()
        for i in range(4):
            ax = a + dy[i]
            ay = b + dx[i]
            if 0 <= ax < N and 0<= ay < M and graph[ax][ay]==1:
                q.append([ax,ay])
                graph[ax][ay] = 0
    result += 1

T = int(input())

for m in range(T):
    M,N,K = map(int,input().split())
    result = 0
    graph = [[0]*(M) for i in range(N)]

    for i in range(K):
        a,b = map(int,input().split())
        graph[b][a] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
    print(result)
