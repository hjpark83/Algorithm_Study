# Question: BJ 1890 (https://www.acmicpc.net/problem/1890)
# Rank : Silver1
# Algorithm : DP
import sys
input = sys.stdin.readline

n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
DP = [[0] * n for _ in range(n)]

DP[0][0] = 1

for i in range(n):
    for j in range(n):
        if Map[i][j] == 0:
            continue
        if i + Map[i][j] < n:
            DP[i + Map[i][j]][j] += DP[i][j]
        if j + Map[i][j] < n:
            DP[i][j + Map[i][j]] += DP[i][j]

print(DP[-1][-1])