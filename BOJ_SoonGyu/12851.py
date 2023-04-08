import sys
from collections import deque
input = sys.stdin.readline
#17626

N,K = map(int,input().split())
result_way = 0
visited = [-1] * 100001
visited[N] = 0

def bfs(v):
    global result_way
    q = deque()
    q.append(v)

    while q:
        place = q.popleft()

        if place == K:
            result_way += 1

        for next_place in [place-1,place+1,place*2]:
            if 0 <= next_place < 100001:
                if visited[next_place] == -1 or visited[next_place] >= visited[place] + 1:
                    q.append(next_place)
                    visited[next_place] = visited[place] + 1

bfs(N)
print(visited[K])
print(result_way)


