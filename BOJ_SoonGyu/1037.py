import sys
#1037
input = sys.stdin.readline

N = int(input())
data= list(map(int,input().split()))

num1 = max(data)
num2 = min(data)

print(num1 * num2)
