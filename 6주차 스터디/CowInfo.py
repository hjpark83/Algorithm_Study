# Question: BJ 17128 (https://www.acmicpc.net/problem/17128)
# Rank : Silver2
# Algorithm : Math, Implementation, Aggregation
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
Cows = list(map(int, input().split()))
Answer = [0]*N

for i in range(N):
    Answer[i] = Cows[i]*Cows[i-1]*Cows[i-2]*Cows[i-3] # 각 소의 점수 계산

Index = list(map(int, input().split()))
Sum = sum(Answer) # 초기 점수 합계 계산
for idx in Index:
    for i in range(4):
        new_idx = (idx-1+i)%N # 인덱스 계산 (0~N-1 사이의 값으로 변경)
        Answer[new_idx] *= -1 # 부호 변경
        Sum += 2*Answer[new_idx]
    print(Sum)