import sys
#7785

input = sys.stdin.readline

N = int(input())
data = {}

for i in range(N):
    name, inout = map(str,input().split())

    if inout == "enter":
        data[name] = 'enter'
    else:
        if data[name]:
            del data[name]

data = sorted(data.keys(), reverse=True)

for i in range(len(data)):
    print(data[i])

