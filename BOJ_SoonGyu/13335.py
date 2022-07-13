import sys
#13335

input = sys.stdin.readline

N,W,L = map(int,input().split())

result = 0

data = list(map(int,input().split()))
bridge = [0] * W

while bridge:
    result += 1
    bridge.pop(0)
    if data:
        if sum(bridge) + data[0] <= L:
            bridge.append(data.pop(0))
        else:
            bridge.append(0)
print(result)
