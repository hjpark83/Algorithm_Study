# Question: BJ 2073 (https://www.acmicpc.net/problem/2073)
# Rank: Gold4
# Algorithm: DP, Knapsack

import sys
input = sys.stdin.readline

D, P = map(int, input().split())
DP = [0 for _ in range(D+1)]

for _ in range(P):
    L, C = map(int, input().split())
    for i in reversed(range(D+1)):
        if i>=L:
            DP[i] = max(DP[i], min(DP[i-L], C))
    
    if C > DP[L]:
        DP[L] = C
        
print(DP[-1])