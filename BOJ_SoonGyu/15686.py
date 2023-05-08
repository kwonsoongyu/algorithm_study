import sys
input = sys.stdin.readline
from itertools import combinations
#15686

N,M = map(int,input().split())

house = []
chicken = []
graph = []
result = 100000000

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            house.append([x,y])
        if graph[x][y] == 2:
            chicken.append([x,y])

for i in combinations(chicken,M):
    city_dist = 0
    for j in house:
        house_dist = 100000000
        for k in i:
            house_dist = min(house_dist,abs(j[0]-k[0])+abs(j[1]-k[1]))
        city_dist += house_dist
    result = min(result,city_dist)

print(result)

