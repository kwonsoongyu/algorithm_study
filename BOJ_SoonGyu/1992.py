import sys
input=sys.stdin.readline

N =int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().rstrip())))

def check(row,col,n):
    curr = graph[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != graph[i][j]:
                curr = -1
                break

    if curr == -1:
        print("(",end="")
        next_n = n // 2
        check(row, col, next_n)
        check(row, col+ next_n, next_n)
        check(row + next_n, col, next_n)
        check(row + next_n, col + next_n, next_n)
        print(")",end="")

    elif curr == 1:
        print(1,end="")
    elif curr == 0:
        print(0, end='')

check(0,0,N)

