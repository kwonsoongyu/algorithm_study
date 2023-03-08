import sys
#11403
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

for i in range(N):
    for j in range(N):
        for t in range(N):
            if graph[j][i] == 1 and graph[i][t] == 1:
                graph[j][t] = 1

for i in graph:
    print(*i)
