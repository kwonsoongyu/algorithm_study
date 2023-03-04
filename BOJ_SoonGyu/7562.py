import sys
from collections import deque
#7562
input = sys.stdin.readline

T = int(input())

dx = [2,2,1,1,-2,-2,-1,-1]
dy = [1,-1,2,-2,1,-1,2,-2]


def bfs(x, y, weight, height):
    q = deque()
    q.append([x,y])
    graph[x][y] = 1

    while q:
        a,b = q.popleft()
        if a == weight and b == height:
            print(graph[weight][height]-1)
            return
        for p in range(8):
            ax = a+dx[p]
            ay = b+dy[p]
            if 0 <= ax < i and 0 <= ay < i and graph[ax][ay] == 0:
                q.append([ax,ay])
                graph[ax][ay] = graph[a][b]+1

while T:
    T = T-1

    i = int(input())
    x, y = map(int, input().split())
    weight, height = map(int, input().split())

    graph = [[0]*(i) for t in range(i)]
    bfs(x,y,weight,height)

