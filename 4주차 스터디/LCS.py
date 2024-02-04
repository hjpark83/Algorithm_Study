# Question: BJ 9251 (https://www.acmicpc.net/problem/9251)
# Rank : Gold5
# Algorithm : DP, String
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
DP = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(len(str1)+1):
    for j in range(len(str2)+1):
        if i==0 or j==0:
            DP[i][j]=0
        elif str1[i-1]==str2[j-1]:
            DP[i][j]=DP[i-1][j-1]+1
        else:
            DP[i][j]=max(DP[i-1][j], DP[i][j-1])

print(DP[len(str1)][len(str2)])