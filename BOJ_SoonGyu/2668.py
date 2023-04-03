import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#2668

N = int(input())

graph = [[]*(N+1) for i in range(N+1)]

for i in range(N):
    num = int(input())
    graph[i+1].append(num)


result = []
def dfs(v,number):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i,number)
        elif visited[i] and i == number:
            result.append(i)

for i in range(1,N+1):
    visited = [0] * (N + 1)
    dfs(i,i)

print(len(result))
for i in range(len(result)):
    print(result[i])
