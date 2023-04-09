import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#1240

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A,B,distance = map(int,input().split())
    graph[A].append([B,distance])
    graph[B].append([A,distance])

def dfs(V,target,dist):
    global result
    DFS[V] = True

    for i,distance in graph[V]:
        if not DFS[i]:
            if i == target:
                result = dist + distance
            else:
                dfs(i,target,distance+dist)

for i in range(M):
    A,B = map(int,input().split())
    DFS = [False] * (N + 1)
    result = 0
    dfs(A,B,0)
    print(result)
