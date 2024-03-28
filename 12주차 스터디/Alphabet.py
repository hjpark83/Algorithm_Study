# Question: BJ 1987 (https://www.acmicpc.net/problem/1987)
# Rank: Gold4
# Algorithm: Graph, DFS, Backtracking

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

Map = [[]*C for _ in range(R)]

for i in range(R):
    Map[i] = list(input().rstrip())
        
def InRange(x, y):
    return 0 <= x < R and 0 <= y < C    

def DFS():
    global ans
    x, y, cnt = 0, 0, 1
    stack = set()
    stack.add((x, y, cnt, Map[x][y]))
    while stack:
        x, y, cnt, visited = stack.pop()
        ans = max(ans, cnt)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if InRange(nx, ny) and Map[nx][ny] not in visited:
                stack.add((nx, ny, cnt+1, visited+Map[nx][ny]))
                
ans = 0
DFS()
print(ans)
        