import sys
input = sys.stdin.readline
from collections import deque
#16928

N, M = map(int,input().split())
board = [0] * 101
visited = [False] * 101

snake = dict()
ladder = dict()
for _ in range(N):
    i,j = map(int,input().split())
    ladder[i] = j
for _ in range(M):
    i,j = map(int,input().split())
    snake[i] = j


queue = deque([1])
visited[1] = True
while queue:
    now = queue.popleft()
    for move in range(1,7):
        check_move = now+move
        if 0 < check_move <= 100 and not visited[check_move]:
            if check_move in ladder.keys():
                check_move = ladder[check_move]

            if check_move in snake.keys():
                check_move = snake[check_move]

            if not visited[check_move]:
                queue.append(check_move)
                visited[check_move] = True
                board[check_move] = board[now] + 1

print(board[100])
