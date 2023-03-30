import sys
input = sys.stdin.readline
#1107

N = int(input())
M = int(input())
breakdown = list(map(int,input().split()))
mincount = abs(100-N)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in breakdown:
            break

        elif j == len(num) - 1:
            mincount = min(mincount,abs(int(num)-N) + len(num))

print(mincount)
