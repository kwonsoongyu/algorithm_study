import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#1068

N = int(input())
row = list(map(int,input().split()))
result = 0

delete = int(input())


def dfs(V):
    row[V] = -2
    for i in range(N):
        if V == row[i]:
            dfs(i)

dfs(delete)

for i in range(N):
    if row[i] != -2 and i not in row:
        result += 1

print(result)
