import sys
#9461
input = sys.stdin.readline

T = int(input())
result = [[0] for i in range(101)]
result[1] = 1
result[2] = 1
result[3] = 1
for i in range(T):
    num = int(input())
    for j in range(4,101):
        result[j] = result[j-2] + result[j-3]

    print(result[num])
