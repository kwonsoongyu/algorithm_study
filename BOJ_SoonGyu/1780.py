import sys
#1780
input = sys.stdin.readline

N = int(input())
minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

graph = []

for i in range(N):
    row = list(map(int,input().rsplit()))
    graph.append(row)

def check(row,col,n):
    global minus_cnt,plus_cnt,zero_cnt
    #현재 종이 색상
    curr = graph[row][col]

    for i in range(row, row+n):
        for j in range(col,col+n):
            if graph[i][j] != curr:
                next_n = n // 3
                check(row,col,next_n)
                check(row,col+next_n,next_n)
                check(row,col+(2*next_n),next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                check(row + next_n,col + (2*next_n),next_n)
                check(row+(2*next_n),col,next_n)
                check(row+(2*next_n),col+next_n,next_n)
                check(row + (2*next_n), col + (2*next_n), next_n)
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1

check(0,0,N)
print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
