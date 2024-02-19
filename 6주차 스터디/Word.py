# Question: BJ 9081 (https://www.acmicpc.net/problem/9081)
# Rank : Silver1
# Algorithm : Math, Implementation, String, Permutation
import sys
input = sys.stdin.readline

def FindNextPermutation(s):
    k = -1
    for i in range(len(s)-2, -1, -1):
        if s[i] < s[i+1]: # 첫번째 index 찾기
            k = i
            break
    if k == -1: # 더이상 다음 순열이 없는 경우
        return s
    l = -1 
    for i in range(len(s)-1, k, -1): # 두번째 index 찾기
        if s[i] > s[k]: 
            l = i
            break
    s[k], s[l] = s[l], s[k] # 두 index의 값을 바꾸기
    s[k+1:] = reversed(s[k+1:]) # k+1부터 끝까지 뒤집기
    return s

T = int(input())
new_list = []
for _ in range(T):
    word = list(input().strip())
    next_word = FindNextPermutation(word)
    if next_word:
        print(''.join(next_word))
    else:
        print(''.join(word))