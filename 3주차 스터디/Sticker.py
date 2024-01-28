# Question: BJ 9465 (https://www.acmicpc.net/problem/9465)
# Rank : Silver1
# Algorithm : DP

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    DP = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    
    if N > 1:
        DP[0][1] += DP[1][0]
        DP[1][1] += DP[0][0]
    
    for i in range(2,N):
        DP[0][i] += max(DP[1][i-1],DP[1][i-2])
        DP[1][i] += max(DP[0][i-1],DP[0][i-2])
        
    print(max(DP[0][N-1 if N > 1 else 0], DP[1][N-1 if N > 1 else 0]),end="\n")