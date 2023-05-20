import sys
input = sys.stdin.readline
from collections import deque
#15662

T = int(input())
graph = deque()
result = 0

for i in range(T):
    row = deque(map(int,input().rstrip()))
    graph.append(row)

K = int(input())

for i in range(K):
    num, dir = map(int,input().split())
    rotating=[[0],[0],[0],[0]]
    numbering = []
    Rcheck = False
    Lcheck = False
    for j in range(T-1):
        if graph[j][2] == graph[j+1][6]:
            numbering.append(False)
        else:
            numbering.append(True)

    #오른쪽
    for j in range(num,T):
        if numbering[j-1] == False:
            break
        else:
            if dir == 1:
                if Rcheck == False:
                    graph[j].rotate(-1)
                    Rcheck = True
                else:
                    graph[j].rotate(1)
                    Rcheck = False
            else:
                if Rcheck == False:
                    graph[j].rotate(1)
                    Rcheck = True
                else:
                    graph[j].rotate(-1)
                    Rcheck = False

    #왼쪽
    for j in range(num,1,-1):
        if numbering[j-2] == False:
            break
        else:
            if dir == 1:
                if Lcheck == False:
                    graph[j-2].rotate(-1)
                    # print(graph)
                    Lcheck = True
                else:
                    graph[j-2].rotate(1)
                    Lcheck = False
            else:
                if Lcheck == False:
                    graph[j-2].rotate(1)
                    Lcheck = True
                else:
                    graph[j-2].rotate(-1)
                    Lcheck = False
    if dir == 1:
        graph[num-1].rotate(1)
    else:
        graph[num-1].rotate(-1)

for i in range(T):
    if graph[i][0] == 1:
        result += 1

print(result)
