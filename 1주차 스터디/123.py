# Question: BJ 9095 (https://www.acmicpc.net/problem/9095)
# Rank : Silver 3
# Algorithm : DP

import sys
input=sys.stdin.readline
N=int(input())

for _ in range(N):
    T=int(input())
    DP=[0]*(T+1)
    
    for i in range(1,T+1):
        if i==1:
            DP[i]=1
        elif i==2:
            DP[i]=2
        elif i==3:
            DP[i]=4
        else:
            DP[i]=DP[i-1]+DP[i-2]+DP[i-3]
    
    print(DP[T])