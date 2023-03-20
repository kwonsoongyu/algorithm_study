import sys
input=sys.stdin.readline

N = int(input())
graph = list(map(int,input().split()))

graph2 = sorted(list(set(graph)))

dic = {}

for i in range(len(graph2)):
    dic[graph2[i]] = i

for i in graph:
    print(dic[i], end=" ")
