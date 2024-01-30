# Question: BJ 2615 (https://www.acmicpc.net/problem/2615)
# Rank : Silver1
# Algorithm : Implementation, Brute-force

import sys
board=[]

for i in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))
    
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

find =False
for x in range(19):
    for y in range(19):
        if board[x][y] !=0:
            target = board[x][y]
            
            for k in range(4):
                cnt=1
                nx = x+dx[k]
                ny = y+dy[k]
                
                while 0<=nx<19 and 0<=ny<19 and board[nx][ny]==target:
                    cnt+=1
                    if cnt==5:
                        # 6목 체크
                        if 0<=x-dx[k]<19 and 0<=y-dy[k]<19 and board[x-dx[k]][y-dy[k]]==target:
                            break
                        if 0<=nx+dx[k]<19 and 0<=ny+dy[k]<19 and board[nx+dx[k]][ny+dy[k]]==target:
                            break
                        print(target)
                        print(x+1, y+1)
                        find=True
                        sys.exit()
                    
                    nx += dx[k]
                    ny += dy[k]
                    
if not find:
    print(0)