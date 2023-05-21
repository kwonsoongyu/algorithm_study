import sys
input = sys.stdin.readline

#1932

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == len(graph[i])-1:
            graph[i][j] += graph[i-1][j-1]
        else:
            num1 = graph[i][j] + graph[i-1][j-1]
            num2 = graph[i][j] + graph[i-1][j]
            graph[i][j] = max(num1,num2)

print(max(graph[N-1]))


