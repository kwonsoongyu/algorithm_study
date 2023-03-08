import sys
from collections import deque
#5430
input = sys.stdin.readline

T = int(input())

for i in range(T):
    word = str(input().rstrip())
    num = int(input())
    arr = input().rstrip()[1:-1].split(',')
    q = deque(arr)
    flag = 1

    if num == 0:
        q = []

    Rnum = 0

    for j in word:
        if j == 'R':
            Rnum += 1
        if j =='D':
            if len(q) == 0:
                print("error")
                flag = 0
                break
            else:
                if Rnum % 2 ==0:
                    q.popleft()
                else:
                    q.pop()
    if flag == 0:
        continue
    else:
        if Rnum % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
