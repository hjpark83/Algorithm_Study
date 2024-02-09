# Question: BJ 13164 (https://www.acmicpc.net/problem/13164)
# Rank : Gold5
# Algorithm : Greedy, Sorting
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
price = list(map(int, input().split()))

price.sort()
diff = []

for i in range(1, N):
    diff.append(price[i]-price[i-1])
    
diff.sort()
print(sum(diff[:N-K]))