# Question: BJ 14889 (https://www.acmicpc.net/problem/14889)
# Rank: Silver1
# Algorithm: Brute-force, Backtracking

import sys
input = sys.stdin.readline

N = int(input())
S = []

for _ in range(N):
    S.append(list(map(int, input().split())))

min_diff = float('inf')

# N = 4일 때 1, 2번이 Start team -> 3, 4번이 Rink team
# N = 6일 때 1, 3, 4번이 Start team -> 2, 5, 6번이 Rink team
def make_teams(team_start, cnt, idx):
    global min_diff
    if idx == N:
        if cnt == N//2:
            team_link = []
            for i in range(N):
                if i not in team_start:
                    team_link.append(i)
                    
            start_power = calculate_power(team_start)
            link_power = calculate_power(team_link)
            diff = abs(start_power - link_power)
            min_diff = min(min_diff, diff)
        return
    
    if cnt < N//2:
        team_start.append(idx)
        make_teams(team_start, cnt+1, idx+1)
        team_start.pop() # 백트래킹
    
    make_teams(team_start, cnt, idx+1)
    
def calculate_power(team):
    power = 0
    for i in team:
        for j in team:
            power += S[i][j]
    return power

make_teams([], 0, 0)
print(min_diff)