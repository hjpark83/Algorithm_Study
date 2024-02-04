# Question: BJ 1316 (https://www.acmicpc.net/problem/1316)
# Rank : Silver5
# Algorithm : Implementation, String
import sys
input = sys.stdin.readline
N=int(input())

word=[]
for i in range(N):
    word.append(input().strip())
    
for i in range(len(word)):
    for j in range(len(word[i])-1):
        if word[i][j] == word[i][j+1]:
            pass
        elif word[i][j] in word[i][j+1:]:
            N-=1
            break

print(N)