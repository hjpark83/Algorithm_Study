# Question: BJ 16234 (https://www.acmicpc.net/problem/16234)
# Rank: Gold4
# Algorithm: Implementation, Graph, Simulation, BFS 

from sys import stdin
from collections import deque

input = stdin.readline

N, L, R = map(int, input().split())
Country = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    union = []
    union.append((start_x, start_y))
    visited[start_x][start_y] = True
    total_population = Country[start_x][start_y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if inRange(nx, ny) and not visited[nx][ny]:
                if L <= abs(Country[x][y] - Country[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += Country[nx][ny]
    return union, total_population

def move_people():
    days = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        flag = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    union, total_population = bfs(i, j, visited)
                    if len(union) > 1:
                        flag = True
                        avg_population = total_population // len(union)
                        for x, y in union:
                            Country[x][y] = avg_population
        if not flag:
            break
        days += 1
    return days

print(move_people())
