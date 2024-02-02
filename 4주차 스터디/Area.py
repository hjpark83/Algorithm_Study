# Question: BJ 2583 (https://www.acmicpc.net/problem/2583)
# Rank : Silver1
# Algorithm : Graph, BFS, DFS
import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
Map = [[0 for i in range(N)] for j in range(M)]
visited = [[False for i in range(N)] for j in range(M)]
result = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(M-y2, M-y1):
        for i in range(x1, x2):
            Map[j][i] = 1     
    
def BFS(start_y, start_x):
    queue=deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True
    cnt = 1
    
    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and Map[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    result.append(cnt)
                
for j in range(M):
    for i in range(N):
        if not visited[j][i] and Map[j][i] == 0:
            BFS(j, i)
            
print(len(result))
result.sort()
print(*result)