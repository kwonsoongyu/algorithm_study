import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)

for i in range(M):
    start,end,cost = map(int,input().split())
    graph[start].append([end,cost])

start,end = map(int,input().split())

dist[start] = 0
heap = []

heapq.heappush(heap,[0,start])
while heap:
    curr_cost,curr_node = heapq.heappop(heap)

    if dist[curr_node] < curr_cost:
        continue
        
    for next_node,next_cost in graph[curr_node]:
        total_cost = next_cost + curr_cost
        if total_cost < dist[next_node]:
            dist[next_node] = total_cost
            heapq.heappush(heap,[total_cost,next_node])

print(dist[end])

