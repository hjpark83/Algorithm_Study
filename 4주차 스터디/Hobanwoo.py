# Question: BJ 20117 (https://www.acmicpc.net/problem/20117)
# Rank : Silver1
# Algorithm : Greedy, Sorting
import sys
input = sys.stdin.readline

N=int(input())
Quality = list(map(int, input().split()))

Quality.sort()

mid=0
if N%2==0: # 짝수개
    for i in range(N//2):
        mid+=Quality[N-i-1]*2
else: # 홀수개
    for i in range(N//2):
        mid+=Quality[N-i-1]*2
    mid+=Quality[N//2]
    
print(mid)