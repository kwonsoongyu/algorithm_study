import sys
#1764
input = sys.stdin.readline

N,M = map(int,input().split())

data1=[]
data2=[]

for i in range(N):
    data1.append(input().rstrip())
my_data1 = set(data1)

for i in range(M):
    data2.append(input().rstrip())
my_data2 = set(data2)

result = my_data1 & my_data2
result1 = list(result)
result1.sort()

print(len(result1))

for i in range(len(result1)):
    print(result1[i])
