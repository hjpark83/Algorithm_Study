# Question: BJ 20922 (https://www.acmicpc.net/problem/20922)
# Rank: Silver 1
# Algorithm: Two Pointer

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 각 숫자가 나타난 횟수를 저장하는 딕셔너리
count = {}
left, right = 0, 0
max_length = 0

while right < N:
    num = A[right]
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    
    # 현재 창의 길이가 K를 초과하면 왼쪽 포인터를 이동시킴
    while count[num] > K:
        count[A[left]] -= 1
        left += 1
    
    max_length = max(max_length, right-left+1)
    right += 1

print(max_length)
