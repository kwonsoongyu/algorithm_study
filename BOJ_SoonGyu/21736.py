import sys
sys.setrecursionlimit(10**6)
#21736
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[0]*M for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
target = []

for i in range(N):
    col = list(input().rstrip())
    for c in range(len(col)):
        if col[c] == "I":
            target = [i,c]
    board.append(col)

count = 0

def dfs(x,y):
    global count
    if 0<= x < N and 0 <= y < M and not graph[x][y]:
        graph[x][y] = 1
        if board[x][y] == 'P':
            count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M and not graph[nx][ny]:
                if board[nx][ny] != 'X':
                    dfs(nx,ny)

dfs(target[0],target[1])

if not count:
    print("TT")
else:
    print(count)
