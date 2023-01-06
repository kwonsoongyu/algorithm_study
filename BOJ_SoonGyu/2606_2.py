import sys
#2606
input = sys.stdin.readline

M = int(input())
N = int(input())
result = 0
graph = [[0]*(M+1) for i in range(M+1)]

for i in range(N):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS = [0]*(M+1)

def dfs(v):
    global result
    DFS[v] = 1
    result += 1
    for i in range(M+1):
        if not DFS[i] and graph[v][i]:
            dfs(i)
    return result
end = dfs(1)
print(end-1)
