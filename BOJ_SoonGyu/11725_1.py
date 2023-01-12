#dfs
import sys
sys.setrecursionlimit(10**6)
from collections import deque
#11725
input = sys.stdin.readline

N = int(input())
graph =[[] for i in range(N+1)]
result = []
num = 0
for i in range(N-1):
    num1, num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

DFS = [0] * (N+1)

def dfs(v):
    for i in graph[v]:
        if not DFS[i]:
            DFS[i] = v
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(DFS[i])
