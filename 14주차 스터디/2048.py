# Question: BJ 12100 (https://www.acmicpc.net/problem/12100)
# Rank: Gold2
# Algorithm: Implementation, Simulation, Brute-force, Backtracking

import sys
input = sys.stdin.readline

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def move(board, direction):
    if direction == 0: # 왼쪽
        for i in range(N):
            row = [x for x in board[i] if x]
            for j in range(1, len(row)): # 왼쪽부터 탐색
                if row[j] == row[j-1]:
                    row[j-1] *= 2
                    row[j] = 0
            row = [x for x in row if x]
            board[i] = row + [0]*(N-len(row)) # ex) 2 2 0 0 -> 4 0 0 0
    elif direction == 1: # 오른쪽
        for i in range(N):
            row = [x for x in board[i] if x]
            for j in range(len(row)-2, -1, -1): # 오른쪽부터 탐색
                if row[j] == row[j+1]:
                    row[j+1] *= 2
                    row[j] = 0
            row = [x for x in row if x]
            board[i] = [0]*(N-len(row)) + row  # ex) 0 0 2 2 -> 0 0 0 4
    elif direction == 2: # 위쪽
        board = Transpose(board)
        for i in range(N):
            row = [x for x in board[i] if x]
            for j in range(1, len(row)):
                if row[j] == row[j-1]:
                    row[j-1] *= 2
                    row[j] = 0
            row = [x for x in row if x]
            board[i] = row + [0]*(N-len(row))
        board = Transpose(board)
    else: # 아래쪽
        board = Transpose(board)
        for i in range(N):
            row = [x for x in board[i] if x]
            for j in range(len(row)-2, -1, -1):
                if row[j] == row[j+1]:
                    row[j+1] *= 2
                    row[j] = 0
            row = [x for x in row if x]
            board[i] = [0]*(N-len(row)) + row
        board = Transpose(board)
    return board

def Transpose(board):
    newBoard = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newBoard[j][i] = board[i][j]
    return newBoard

def moveAll(board, depth):
    if depth == 5:
        return max([max(row) for row in board]) # 행에서의 최댓값 -> 전체에서의 최댓값
    ret = 0
    for i in range(4):
        newBoard = move([row[:] for row in board], i) # 1번 이동한 board
        ret = max(ret, moveAll(newBoard, depth+1)) # 그때그때 최대값을 갱신
    return ret

print(moveAll(Board, 0))
                        