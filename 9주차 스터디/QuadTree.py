# Question: BJ 1992 (https://www.acmicpc.net/problem/1992)
# Rank: Silver1
# Algorithm: Divide and Conquer, Recursion
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

def quadtree(x, y, n):
    if n == 1:
        return str(arr[x][y]) # 1x1일 때는 그냥 반환
    result = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]: # 4등분한 사각형 중 하나라도 다른 숫자가 있으면
                result.append('(')
                result.extend(quadtree(x, y, n//2)) # 왼쪽 위 사각형
                result.extend(quadtree(x, y+n//2, n//2)) # 오른쪽 위 사각형
                result.extend(quadtree(x+n//2, y, n//2)) # 왼쪽 아래 사각형
                result.extend(quadtree(x+n//2, y+n//2, n//2)) # 오른쪽 아래 사각형
                result.append(')')
                return result
    return str(arr[x][y])

print(''.join(quadtree(0, 0, N)))