import sys
input = sys.stdin.readline
import heapq
# 2573

inf = sys.maxsize
T = int(input())

def dijkstra(V):
    count = 0
    heap = [(0,V)]
    distance = [inf] * (N + 1)
    distance[V] = 0

    while heap:
        curr_cost,curr_node = heapq.heappop(heap)
        if curr_cost > distance[curr_node]:
            continue
        for next_node,next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,(total_cost,next_node))

    ans = []
    for i in range(1, len(distance)):
        if distance[i] != inf:
            ans.append(distance[i])
            count += 1

    last_node= max(ans)

    print(count,last_node)

for i in range(T):
    N,D,C = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    for j in range(D):
        a,b,s = map(int,input().split())
        graph[b].append([a,s])

    dijkstra(C)



