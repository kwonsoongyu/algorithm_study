import sys
from collections import deque
#1697
input = sys.stdin.readline

dx = [1,-1,2]
def bfs(x):
    q = deque([x])
    while q:
        v = q.popleft()
        if v == K:
            return result[v]
        for i in (v-1, v+1, 2*v):
            if 0<= i < 100001 and not result[i]:
                result[i] = result[v] + 1
                q.append(i)

N,K = map(int,input().split())
result = [0] * 100001
print(bfs(N))
