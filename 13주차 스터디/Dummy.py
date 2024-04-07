# Question: BJ 3190 (https://www.acmicpc.net/problem/3190)
# Rank: Gold4
# Algorithm: Implementation, Data Structure, Simulation, Deque, Queue

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
    
L = int(input())
directions = deque()
for _ in range(L):
    x, c = input().split()
    directions.append((int(x), c))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque()
snake.append((0, 0))
board[0][0] = 2 # 뱀
direction = 0
time = 0

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

while True:
    time += 1
    x, y = snake[-1] # 머리 위치
    nx, ny = x + dx[direction], y + dy[direction] 
    
    if not inRange(nx, ny) or board[nx][ny] == 2: # 벽에 부딪히거나 자기 자신과 부딪히면
        break
    elif board[nx][ny] == 0: # 사과가 없으면
        tx, ty = snake.popleft()
        board[tx][ty] = 0 
        
    snake.append((nx, ny))
    board[nx][ny] = 2
    
    if directions and time == directions[0][0]:
        x, c = directions.popleft()
        if c == 'L':
            direction = (direction - 1) % 4 # 왼쪽으로 90도 회전
        else:
            direction = (direction + 1) % 4 # 오른쪽으로 90도 회전
            
print(time)
