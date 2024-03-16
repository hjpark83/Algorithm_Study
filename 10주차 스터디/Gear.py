# Question: BJ 14891 (https://www.acmicpc.net/problem/14891)
# Rank: Gold 5
# Algorithm: Implementation, Simulation

import sys
input = sys.stdin.readline

input_gear = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

def rotate(gear, direction):
    if direction == 1:
        gear = [gear[-1]] + gear[:-1] # 시계방향
    else:
        gear = gear[1:] + [gear[0]] # 반시계방향
    return gear

def solve(gear, direction):
    directions = [0] * 4
    directions[gear] = direction
    for i in range(gear, 3):
        if input_gear[i][2] != input_gear[i+1][6]: # 오른쪽 톱니바퀴와 맞닿은 부분이 다르면
            directions[i+1] = -directions[i] # 반대방향으로 회전
        else:
            break
    for i in range(gear, 0, -1): 
        if input_gear[i][6] != input_gear[i-1][2]: # 왼쪽 톱니바퀴와 맞닿은 부분이 다르면 
            directions[i-1] = -directions[i] # 반대방향으로 회전
        else:
            break
    for i in range(4):
        if directions[i] != 0:
            input_gear[i] = rotate(input_gear[i], directions[i]) # 회전방향에 따라 톱니바퀴 회전
            
for _ in range(K):
    gear, direction = map(int, input().split())
    solve(gear-1, direction) 
    
answer = 0
for i in range(4):
    if input_gear[i][0] == 1: # S극이면
        answer += 2**i
print(answer)