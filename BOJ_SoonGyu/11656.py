import sys
#11656

input = sys.stdin.readline

data = input().rstrip()

result = []

for i in range(len(data)):
    result.append(data[i:])

result.sort()
for i in range(len(data)):
    print(result[i])

