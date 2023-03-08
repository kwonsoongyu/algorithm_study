import sys
from collections import deque
#10026
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    word = graph[x][y]
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            ax = dx[i] + ax
            ay = dy[i] + ay
            if 0 <= ax < T and 0 <= ay < T and not visited[ax][ay]:
                if word == graph[ax][ay]:
                    q.append([(ax, ay)])
                    visited[ax][ay] = 1


T = int(input())
RGB = 0
RB = 0
visited = [[0] * T for i in range(T)]
graph = [list(map(str,input().strip())) for i in range(T)]

#정상인
for i in range(T):
    for j in range(T):
        if not visited[i][j]:
            bfs(i, j)
            RGB += 1

visited = [[0] * T for i in range(T)]
#적록색맹
for i in range(T):
    for j in range(T):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(T):
    for j in range(T):
        if not visited[i][j]:
            bfs(i,j)
            RB += 1

print(RGB,RB)
