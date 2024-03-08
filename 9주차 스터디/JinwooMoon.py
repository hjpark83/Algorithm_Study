# Question: BJ 17485 (https://www.acmicpc.net/problem/17485)
# Rank: Gold5
# Algorithm: DP

import sys
input = sys.stdin.readline

INF = 10**9
N, M = map(int, input().split())
Dist = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0] * 3 for _ in range(M)] for _ in range(N)]
for j in range(M):
    for k in range(3):
        DP[0][j][k] = Dist[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 0) or (j == M-1 and k == 2):
                DP[i][j][k] = INF
                continue
            if k == 0:
                DP[i][j][k] = min(DP[i-1][j-1][1], DP[i-1][j-1][2]) + Dist[i][j]
            elif k == 1:
                DP[i][j][k] = min(DP[i-1][j][0], DP[i-1][j][2]) + Dist[i][j]
            else:
                DP[i][j][k] = min(DP[i-1][j+1][0], DP[i-1][j+1][1]) + Dist[i][j]

result = INF
for j in range(M):
    result = min(result, min(DP[-1][j]))
print(result)