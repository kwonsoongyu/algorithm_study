import sys
#1166
input = sys.stdin.readline

N,L,W,H = map(int,input().split())

start = 0
end = max(L,W,H)

for i in range(10000):
    mid = (start + end) / 2

    num = (W // mid) * (H // mid) * (L // mid)

    if num >= N:
        start = mid
    else:
        end = mid

print("%.10f" %(end))
