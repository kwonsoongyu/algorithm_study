import sys
input = sys.stdin.readline
from collections import deque
#9019

T = int(input())

for i in range(T):
    A,B = map(int,input().rstrip().split())
    q = deque()
    q.append([A,""])
    visited = [False for _ in range(10001)]
    visited[A] = True

    while q:
        num,word = q.popleft()
        visited[num] = True

        if num == B:
            print(word)
            break

        #D
        d = num * 2 % 10000
        if not visited[d]:
            q.append([d,word+"D"])
            visited[d] = True
        #S
        s = (num-1)%10000
        if not visited[s]:
            q.append([s,word+"S"])
            visited[s] = True

        #L
        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            q.append([l,word+"L"])
            visited[l] = True

        #R
        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            q.append([r,word+"R"])
            visited[r] = True

