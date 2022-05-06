import sys
#1427
input = sys.stdin.readline

num = input()
data=[]
for i in range(len(num)-1):
    data.append(num[i])
data.sort(reverse=True)

for i in range(len(data)):
    print(data[i], end="")

