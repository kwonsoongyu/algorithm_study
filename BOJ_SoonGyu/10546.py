import sys
#10546

input = sys.stdin.readline

N = int(input())
data = []
result = []
check = False
for i in range(N):
    name = input().rstrip()
    data.append(name)

for i in range(N-1):
    name = input().rstrip()
    result.append(name)

data.sort()
result.sort()

for i in range(N-1):
    if data[i] != result[i]:
        print(data[i])
        check = True
        break

if check == False:
    print(data[-1])
