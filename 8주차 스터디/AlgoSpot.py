# Question: BJ 1261 (https://www.acmicpc.net/problem/1261)
# Rank: Gold4
# Algorithm: Graph, Dijkstra

import sys
import heapq
input = sys.stdin.readline

M, N = map(int, input().split())
Map = [list(map(int, input().strip())) for _ in range(N)]
dist = [[1e9]*M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra():
    Q = []
    heapq.heappush(Q, (0, 0, 0))
    dist[0][0] = 0
    while Q:
        cost, x, y = heapq.heappop(Q)
        
        if dist[x][y] < cost:
            continue
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                ncost = cost + Map[nx][ny]
                if dist[nx][ny] > ncost:
                    dist[nx][ny] = ncost
                    heapq.heappush(Q, (ncost, nx, ny))
                    
dijkstra()
print(dist[N-1][M-1])