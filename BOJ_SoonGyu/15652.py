import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#15652

N,M = map(int,input().split())
graph = []
def dfs(v):
    if len(graph) == M:
        print(' '.join(map(str,graph)))
        return

    for i in range(v,N+1):
        graph.append(i)
        dfs(i)
        graph.pop()
dfs(1)
