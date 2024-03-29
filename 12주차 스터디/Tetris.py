# Question: BJ 4920 (https://www.acmicpc.net/problem/4920)
# Rank: Gold4
# Algorithm: Implementation, Brute Force

import sys

input = sys.stdin.readline

Shape = [
    # 13가지
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # ㄹ
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (1, 0), (1, 1), (2, 0)],  # ㅏ
    [(0, 1), (1, 0), (1, 1), (2, 1)],  # ㅓ
    [(0, 1), (1, 0), (1, 1), (1, 2)],  # ㅗ
    [(0, 0), (0, 1), (0, 2), (1, 1)]   # ㅜ
]


def inRange(x, y):
    global N
    return 0 <= x < N and 0 <= y < N


def Tetris(x, y):
    global ans
    for i in range(13):
        flag = True
        sum = 0
        for j in range(4):
            nx = x + Shape[i][j][0]
            ny = y + Shape[i][j][1]
            if not inRange(nx, ny):
                flag = False
                break
            sum += Map[nx][ny]
        
        if flag:
            ans = max(ans, sum)

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    ans = -987654321
    Map = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            Tetris(i, j)
            
    print(f"{cnt}. {ans}")
    cnt += 1