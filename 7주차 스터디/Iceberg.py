# Question: BJ 2573 (https://www.acmicpc.net/problem/2573)
# Rank: Gold4
# Algorithm: Implementation, Graph, DFS, BFS

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고 (nx,ny)가 빙하이면서 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ice[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                
def melt():
    new_ice = [[0] * M for _ in range(N)] # 녹은 빙하의 정보를 담을 배열
    for i in range(N):
        for j in range(M):
            if ice[i][j]: # 빙하인 경우
                cnt = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    # ni, nj가 범위 내에 있고 빙하가 아닌 경우
                    if 0 <= ni < N and 0 <= nj < M and not ice[ni][nj]:
                        cnt += 1 # 녹은 빙하이기 때문에 cnt를 1 증가시킴
                new_ice[i][j] = max(0, ice[i][j]-cnt) # 녹은 빙하의 수를 저장
    return new_ice

def check():
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 빙하이고 방문하지 않았다면
            if ice[i][j] and not visited[i][j]:
                bfs(i, j, visited) # bfs로 확인
                cnt += 1
    return cnt

year = 0
while True:
    cnt = check()
    if cnt >= 2: # 빙하가 분리된 경우
        print(year)
        break
    if cnt == 0: # 빙하가 없는 경우
        print(0)
        break
    ice = melt() 
    year += 1