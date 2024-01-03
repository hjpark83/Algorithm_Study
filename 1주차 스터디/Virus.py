# Question: BJ 2606 (https://www.acmicpc.net/problem/2606)
# Rank : Silver 3
# Algorithm : DFS/BFS

N=int(input())
M=int(input())

G=[[] for _ in range(N+1)]
visited=[False]*(N+1)
cnt=-1

for i in range(M):
    s,e=map(int, input().split())
    G[s].append(e);
    G[e].append(s);

def DFS(v):
    visited[v]=True
    global cnt
    cnt+=1
    for i in G[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(cnt)