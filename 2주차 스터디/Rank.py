# Question: BJ 2012 (https://www.acmicpc.net/problem/2012)
# Rank : Silver3
# Algorithm : Sorting, Greedy

import sys

N=int(sys.stdin.readline()) # int를 안씌우면 str도 입력가능해서 오류가뜸
A=[int(sys.stdin.readline()) for i in range(N)]
Rank=[i for i in range(1,N+1)]

A.sort()
ans=0
for i in range(N):
    ans+=abs(A[i]-Rank[i])

print(ans)

# A : 1 5 3 1 2 
#     -> 1 1 2 3 5
# Rank : 1 2 3 4 5
# abs(A[i]-Rank[i]) = 0 1 1 1 0