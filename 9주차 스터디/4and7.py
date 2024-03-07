# Question: BJ 2877 (https://www.acmicpc.net/problem/2877)
# Rank: Gold5
# Algorithm: Math, Implementation

import sys
input = sys.stdin.readline

K = int(input())
result = ''
while K>0:
    m = K%2
    K = K//2
    if m==0:
        K-=1
        result = '7'+result
    else:
        result = '4'+result
print(result)