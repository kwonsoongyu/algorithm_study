import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#1967

N = int(input())
graph = [[] for _ in range(N+1)]
DFS = [-1] * (N+1)


for _ in range(N-1):
    A,B,weight = map(int,input().split())
    graph[A].append([B,weight])
    graph[B].append([A,weight])

def dfs(V,dist):
    for i,distance in graph[V]:
        if DFS[i] == -1:
            DFS[i] = dist+distance
            dfs(i,dist+distance)

dfs(1,0)

start = DFS.index(max(DFS))

DFS = [-1] * (N+1)
DFS[start] = 0
dfs(start,0)
print(max(DFS))
