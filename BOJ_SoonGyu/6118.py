import sys
from collections import deque
input = sys.stdin.readline
#6118

N,M = map(int,input().split())
graph = [[] * (N+1)  for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

BFS = [False] * (N+1) # 7

distance = [0] * (N+1)
def bfs(v):
    q = deque([v])
    BFS[v] = 1
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not BFS[i]:
                q.append(i)
                BFS[i] = True
                distance[i] = distance[v] + 1

bfs(1)

minnum = max(distance)
count = 0
for i in range(len(distance)):
    if minnum == distance[i]:
        count += 1

print(distance.index(minnum),minnum,count,end=" ")

