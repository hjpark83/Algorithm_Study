# Question: BJ 18513 (https://www.acmicpc.net/problem/18513)
# Rank: Gold4
# Algorithm: Data Structure, Graph, BFS

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

house = list(map(int, input().split()))
dict = {}

q = deque()
answer = 0

for i in house:
    dict[i] = 1
    q.appendleft(i)
    
def bfs():
    global answer, K
    while q:
        dx = q.popleft()
        for nx in [dx-1, dx+1]:
            if nx not in dict:
                dict[nx] = dict[dx]+1
                K-=1
                answer += dict[nx]-1
                q.append(nx)
                
                if K==0:
                    print(answer)
                    exit(0)

bfs()