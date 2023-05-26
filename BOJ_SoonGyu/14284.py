import sys
input = sys.stdin.readline
import heapq
#14284

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

S,T = map(int,input().split())

def dijkstra(S,T):
    distance = [100000000000] * (N+1)
    heap = [(0,S)]
    distance[S] = 0

    while heap:
        curr_cost,curr_node = heapq.heappop(heap)
        if distance[curr_node] < curr_cost:
            continue
        for next_node,next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost

            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,(total_cost,next_node))
    return distance[T]

print(dijkstra(S,T))

