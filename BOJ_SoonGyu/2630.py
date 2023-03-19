import sys
from collections import deque
input=sys.stdin.readline

N =int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

blue = 0
white = 0

def check(row,col,n):
    global blue,white
    curr = graph[row][col]

    for i in range(row,row+n):
        for j in range(col,col+n):
            if graph[i][j] != curr:
                next_n = n // 2
                check(row,col,next_n)
                check(row + next_n,col,next_n)
                check(row,col+next_n,next_n)
                check(row+next_n,col+next_n,next_n)
                return
    if curr == 1:
        blue += 1
    elif curr == 0:
        white += 1
check(0,0,N)
print(white)
print(blue)
