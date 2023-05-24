import sys

input = sys.stdin.readline
# 1038
result = []
N = int(input())
maxnum = -10000000000000
minnum = 10000000000
graph = list(map(int, input().split()))
four = list(map(int, input().split()))


def dfs(depth):
    global maxnum, minnum

    if depth == N - 1:
        temp = graph[0]
        for i in range(1, len(graph)):
            mark = result[i - 1]

            if mark == "+":
                temp += graph[i]
            elif mark == "-":
                temp -= graph[i]
            elif mark == "*":
                temp *= graph[i]
            else:
                if temp < 0:
                    rmp = -1 * temp // graph[i]
                    temp = -1 * rmp
                else:
                    temp //= graph[i]

        maxnum = max(temp, maxnum)
        minnum = min(temp, minnum)
    else:
        for j in range(4):
            if four[j] > 0:
                if j == 0:
                    result.append("+")
                elif j == 1:
                    result.append("-")
                elif j == 2:
                    result.append("*")
                elif j == 3:
                    result.append("/")

                four[j] -= 1
                dfs(depth + 1)
                result.pop()
                four[j] += 1


dfs(0)

print(maxnum)
print(minnum)
