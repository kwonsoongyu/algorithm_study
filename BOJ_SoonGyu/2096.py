import sys

input = sys.stdin.readline
#2096

N = int(input())

max_result = [0] * 3
min_result = [0] * 3

max_graph = [0] * 3
min_graph = [0] * 3

for i in range(N):
    a,b,c = map(int,input().split())
    for j in range(3):
        if j == 0:
            max_graph[j] = a + max(max_result[j],max_result[j+1])
            min_graph[j] = a + min(min_result[j],min_result[j+1])
        elif j == 1:
            max_graph[j] = b + max(max_result[j], max_result[j + 1],max_result[j-1])
            min_graph[j] = b + min(min_result[j], min_result[j + 1],min_result[j-1])
        else:
            max_graph[j] = c + max(max_result[j], max_result[j - 1])
            min_graph[j] = c + min(min_result[j], min_result[j - 1])

    for k in range(3):
        max_result[k] = max_graph[k]
        min_result[k] = min_graph[k]

print(max(max_result),min(min_result))
