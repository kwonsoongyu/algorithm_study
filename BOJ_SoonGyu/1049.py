import sys
#1049
input = sys.stdin.readline

N,M = map(int,input().split())
package = []
piece = []
result = []

for i in range(M):
    A, B = map(int,input().split())
    package.append(A)
    piece.append(B)

packmin = min(package)
piecemin = min(piece)

pieceprice = N*piecemin
packprice = (N//6+1)*packmin
originprice = (N//6)*packmin + (N%6)*piecemin

print(min(packprice,originprice,pieceprice))

