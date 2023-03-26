import sys
import heapq
#7662
input = sys.stdin.readline

T = int(input())

for i in range(T):
    K = int(input())
    maxh, minh = [], []
    visited = [False] * K

    for j in range(K):
        word,num = input().split()
        num = int(num)

        if word == 'I':
            heapq.heappush(minh, (num, j))
            heapq.heappush(maxh, (-num, j))
            visited[j] = True
        elif num == 1:
            while maxh and not visited[maxh[0][1]]:
                heapq.heappop(maxh)
            if maxh:
                visited[maxh[0][1]] = False
                heapq.heappop(maxh)
        else:
            while minh and not visited[minh[0][1]]:
                heapq.heappop(minh)
            if minh:
                visited[minh[0][1]] = False
                heapq.heappop(minh)

    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)

    if maxh and minh:
        print(-maxh[0][0],minh[0][0])
    else:
        print("EMPTY")



