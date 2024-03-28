# Question: BJ 2531 (https://www.acmicpc.net/problem/2531)
# Rank: Silver1
# Algorithm: Brute Force, Two pointer, Sliding Window

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]

left, right = 0, 0

sushi_dict = {} # 초밥의 종류를 담는 딕셔너리
sushi_dict[c] = 1 # 쿠폰 초밥은 미리 넣어둔다.

answer = 0

while right < N + k: 
    if right - left < k: # 초밥의 개수가 k보다 작으면 계속 추가
        if sushi[right % N] not in sushi_dict:
            sushi_dict[sushi[right % N]] = 1
        else:
            sushi_dict[sushi[right % N]] += 1
        right += 1
    else:
        if len(sushi_dict) > answer:
            answer = len(sushi_dict)
        if sushi[left % N] in sushi_dict:
            sushi_dict[sushi[left % N]] -= 1
            if sushi_dict[sushi[left % N]] == 0:
                del sushi_dict[sushi[left % N]]
        left += 1
        
print(answer)