# Question: BJ 14502 (https://www.acmicpc.net/problem/14502)
# Rank : Gold4
# Algorithm : Brute Force, Implementation, Graph, BFS
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Map = [[0]*9 for _ in range(9)]
Temp = [[0]*9 for _ in range(9)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = 0

def Input():
    for i in range(N):
        Map[i] = list(map(int, input().split()))
            
def CopyMap(A, B):
    for i in range(N):
        for j in range(M):
            A[i][j] = B[i][j]


def BFS():
    Q = deque()
    for i in range(N):
        for j in range(M):
            if Temp[i][j] == 2:
                Q.append((i,j))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if Temp[nx][ny] == 0:
                    Temp[nx][ny] = 2
                    Q.append((nx,ny))
                    
def GetSafeArea():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Temp[i][j]==0:
                cnt += 1
    return cnt

def DFS(cnt):
    global answer
    if cnt == 3:
        CopyMap(Temp, Map)
        BFS()
        answer = max(answer,GetSafeArea())
        return
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                Map[i][j] = 1 # 벽세우기
                cnt += 1
                DFS(cnt) # 다시 벽세우러 가기
                Map[i][j] = 0 # 벽 허물기
                cnt -= 1
                
def main():
    global N, M, answer
    Input()
    DFS(0)
    print(answer)

if __name__ == "__main__":
    main()