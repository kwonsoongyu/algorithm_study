import sys
from collections import deque
#18352
input = sys.stdin.readline

N,M,K,X = map(int,input().split())

result = []
graph = [[]*(N*1) for i in range(N+1)]
BFS = [0] * (N+1)
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

def bfs(v):
    q = deque([v])
    BFS[v] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not BFS[i]:
                BFS[i] = BFS[v]+1
                if BFS[i] -1 == K:
                    result.append(i)
                q.append(i)

bfs(X)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
