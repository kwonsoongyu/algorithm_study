import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
view = list(map(int,input().split()))
dist = [float('inf')] * (N)
graph = [[] for _ in range(N)]

for i in range(M):
    start,end,cost = map(int,input().split())
    graph[start].append([cost,end])
    graph[end].append([cost,start])

heap = []
heapq.heappush(heap,(0,0))
dist[0] = 0

while heap:
    curr_cost,curr_node = heapq.heappop(heap)

    if dist[curr_node] < curr_cost:
        continue

    for next_cost,next_node in graph[curr_node]:
        total_cost = next_cost + curr_cost

        if next_node == (N-1) and total_cost < dist[next_node]:
            dist[next_node] = total_cost
            heapq.heappush(heap, (total_cost, next_node))
        elif total_cost < dist[next_node] and view[next_node] == 0:
            dist[next_node] = total_cost
            heapq.heappush(heap,(total_cost,next_node))

if dist[-1] == float('inf'):
    print("-1")
else:
    print(dist[-1])
