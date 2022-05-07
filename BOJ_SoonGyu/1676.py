import sys
#1676
input = sys.stdin.readline

N = int(input())
num = 0

while N >= 5:
    num += N // 5

    N = N//5
print(num)
