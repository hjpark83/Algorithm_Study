# Question: BJ 6118 (https://www.acmicpc.net/problem/6118)
# Rank : Silver1
# Algorithm : Graph, BFS

import sys
from collections import deque

graph=[[] for _ in range(20001)]
visited=[-1]*20001

def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                q.append(i)
                
N,M=map(int,sys.stdin.readline().split())
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(1)
max_dist=max(visited)
max_dist_idx=visited.index(max_dist)
max_dist_cnt=visited.count(max_dist)
print(max_dist_idx,max_dist,max_dist_cnt)