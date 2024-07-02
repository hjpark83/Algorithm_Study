# Question: BJ 14888 (https://www.acmicpc.net/problem/14888)
# Rank: Silver1
# Algorithm: Brute Force, Backtracking

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
Op = list(map(int, input().strip().split()))

max_res = float('-inf')
min_res = float('inf')

def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -(-a // b)
        else:
            return a // b
    
def solve(idx, res):
    global max_res, min_res
    if idx == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    for i in range(4):
        if Op[i] > 0:
            Op[i] -= 1
            solve(idx+1, calc(res, A[idx], i))
            Op[i] += 1
            
solve(1, A[0])
print(max_res)
print(min_res)