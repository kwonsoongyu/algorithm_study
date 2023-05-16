import sys
input = sys.stdin.readline
#1149

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(1,len(graph)):
    graph[i][0] = min(graph[i-1][1],graph[i-1][2]) + graph[i][0]
    graph[i][1] = min(graph[i-1][0],graph[i-1][2]) + graph[i][1]
    graph[i][2] = min(graph[i-1][0],graph[i-1][1]) + graph[i][2]

print(min(graph[N-1][0],graph[N-1][1],graph[N-1][2]))

