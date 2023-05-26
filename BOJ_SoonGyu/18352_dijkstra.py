import sys
input = sys.stdin.readline
import heapq
#18352

inf = sys.maxsize
N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [inf] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append([b,1])

def dijkstra(v):
    heap = []
    distance[v] = 0
    heapq.heappush(heap,[0,v])

    while heap:
        curr_cost,curr_node = heapq.heappop(heap)

        for next_node,next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,(total_cost,next_node))

dijkstra(X)
ans = []

for i in range(1,N+1):
    if distance[i] == K:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)
