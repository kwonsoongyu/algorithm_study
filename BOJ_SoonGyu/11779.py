import sys
input = sys.stdin.readline
import heapq
from collections import deque
# 11779
inf = sys.maxsize
N = int(input())
M = int(input())
minnum = 100000000000
minnode = 0
graph = [[] for _ in range(N+1)]
distance = [inf] * (N+1)
ans = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

def dijkstra(S,T):
    heap = [(0,S)]
    distance[S] = 0
    global minnum,minnode
    while heap:
        curr_cost,curr_node = heapq.heappop(heap)

        if distance[curr_node] < curr_cost:
            continue
        for next_node,next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,(total_cost,next_node))
                ans[next_node] = curr_node

    return distance[T]

S,T = map(int,input().split())
print(dijkstra(S,T))
path = []
curr = T

while curr:
    path.append(curr)
    curr = ans[curr]

print(len(path))
for i in path[::-1]:
    print(i,end=" ")

