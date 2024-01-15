# Question: BJ 7576 (https://www.acmicpc.net/problem/7576)
# Rank : Gold5
# Algorithm : Graph, BFS
import sys
from collections import deque

M,N=map(int,input().split())
Graph=[list(map(int,input().split())) for _ in range(N)]
         
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS():
    queue=deque()
    for i in range(N):
        for j in range(M):
            if Graph[i][j]==1:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and Graph[nx][ny]==0:
                Graph[nx][ny]=Graph[x][y]+1
                queue.append((nx,ny))

def main():
    BFS()
    result=0
    for i in range(N):
        for j in range(M):
            if Graph[i][j]==0:
                print(-1)
                return
            result=max(result,Graph[i][j])
    print(result-1)

if __name__=='__main__':
    main()