# Question: BJ 15787 (https://www.acmicpc.net/problem/15787)
# Rank : Silver2
# Algorithm : Implementation, Bitmask
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [0] * n
for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        train[cmd[1]-1] |= (1 << (cmd[2]-1)) # 1을 왼쪽으로 cmd[2]-1만큼 이동
    elif cmd[0] == 2:
        train[cmd[1]-1] &= ~(1 << (cmd[2]-1)) # 1을 왼쪽으로 cmd[2]-1만큼 이동한 것을 반전시킨다.
    elif cmd[0] == 3:
        train[cmd[1]-1] <<= 1 # 1을 왼쪽으로 1만큼 이동
        train[cmd[1]-1] &= (1 << 20) - 1 # 20자리 이하로 자른다.
    else:
        train[cmd[1]-1] >>= 1 # 1을 오른쪽으로 1만큼 이동
        train[cmd[1]-1] &= ~(1 << 20)
        
print(len(set(train))) # 중복을 제거한 후 길이를 출력