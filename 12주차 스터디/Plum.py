# Question: BJ 2240 (https://www.acmicpc.net/problem/2240)
# Rank: Gold5
# Algorithm: DP

import sys
input = sys.stdin.readline

T, W = map(int, input().split())

Plum = [0] + [int(input()) for _ in range(T)]
DP = [[0 for _ in range(W+1)] for _ in range(T+1)]

for i in range(1, T+1):
    if Plum[i] == 1:
        DP[i][0] = DP[i-1][0] + 1
    else:
        DP[i][0] = DP[i-1][0]
        
    for j in range(1, W+1):
        if (Plum[i] == 2 and j%2 == 1) or (Plum[i] == 1 and j%2 == 0):
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + 1
        else:
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])
            
print(max(DP[-1]))
