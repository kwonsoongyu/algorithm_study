import sys
#2579
input = sys.stdin.readline

T = int(input())
stair = [int(input()) for i in range(T)]
graph = [0] * T

if T <= 2:
    print(sum(stair))
else:
    graph[0] = stair[0]
    graph[1] = stair[0] + stair[1]
    for i in range(2,T):
        graph[i] = max((graph[i-2]+stair[i]),graph[i-3]+stair[i-1]+stair[i])
    print(graph[-1])
