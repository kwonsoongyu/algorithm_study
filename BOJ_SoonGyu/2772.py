import sys
from bisect import bisect_left,bisect_right # 이진탐색 모듈
#10815
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    M = int(input())
    B = list(map(int,input().split()))

    A.sort() #이진탐색을 위한 정렬
    result = []

    for i in B:
        left = bisect_left(A,i) #i의 왼쪽 인덱스값
        right = bisect_right(A,i) #i의 오른쪽 인덱스값
        if left == right:
            print(0,end=" ")
        else:
            print(1,end=" ")
