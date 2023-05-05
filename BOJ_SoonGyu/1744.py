import sys
input = sys.stdin.readline
#1744

N = int(input())
plus = []
minus = []
result = []

for i in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        result.append(1)
    else:
        minus.append(num)

plus.sort(reverse= True)
minus.sort()

if len(plus) % 2 == 0:
    for i in range(0,len(plus),2):
        result.append(plus[i]*plus[i+1])
else:
    for i in range(0,len(plus)-1,2):
        result.append(plus[i]*plus[i+1])
    result.append(plus[-1])

if len(minus) % 2 == 0:
    for i in range(0,len(minus),2):
        result.append(minus[i]*minus[i+1])
else:
    for i in range(0,len(minus)-1,2):
        result.append(minus[i]*minus[i+1])
    result.append(minus[-1])

print(sum(result))

