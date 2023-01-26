import sys
from collections import deque
#2667
input = sys.stdin.readline

T = int(input())

sums = []
board = []

for i in range(T):
    board.append(list(map(int,input().rstrip())))

def bfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((x,y))

    board[x][y] = 0
    num = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < T and 0<=ny < T and board[nx][ny]==1:
                board[nx][ny] = 0
                q.append((nx,ny))
                num += 1
    sums.append(num)

for i in range(T):
    for j in range(T):
        if board[i][j] == 1:
            bfs(i,j)

sums.sort()
print(len(sums))

for i in sums:
    print(i)
