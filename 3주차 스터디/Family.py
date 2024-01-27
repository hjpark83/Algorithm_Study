# Question: BJ 2644 (https://www.acmicpc.net/problem/2644)
# Rank : Silver2
# Algorithm : Graph, BFS, DFS
import sys

N=int(sys.stdin.readline())
x,y=map(int, sys.stdin.readline().split())
M=int(sys.stdin.readline())

Family=[[] for _ in range(N+1)]
Visited=[False]*(N+1)

for _ in range(M):
  a,b=map(int, sys.stdin.readline().split())
  Family[a].append(b)
  Family[b].append(a)

def dfs(Family, v,target, Visited, cnt):
    Visited[v]=True
    if v==target: # 현재 노드랑 도착지점이랑 같으면
        return cnt
    for i in Family[v]:
        if not Visited[i]:
            result = dfs(Family, i, target, Visited, cnt+1)
            if result != -1:
                return result
    return -1
            
distance = dfs(Family, x, y, Visited, 0)
print(distance)