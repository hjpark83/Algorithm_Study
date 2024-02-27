# Question: BJ 1283 (https://www.acmicpc.net/problem/1283)
# Rank: Silver1
# Algorithm: Implementation, String

import sys
input = sys.stdin.readline

N=int(input())

shortcut = []
for i in range(N):
    sentence = list(input().rstrip().split())
    
    flag = 0
    data = []
    for j in range(len(sentence)):
        if sentence[j][0].lower() not in shortcut and sentence[j][0].upper() not in shortcut: 
            # 첫 글자가 단축키가 아닌 경우
            shortcut.append(sentence[j][0])
            flag = 1
            sentence[j] = '[' + sentence[j][0] + ']' + sentence[j][1:]
            break
        
    if flag == 0:
        for j in range(len(sentence)):
            flag = 0
            for k in range(len(shortcut)):
                if sentence[j][k].lower() not in shortcut and sentence[j][k].upper() not in shortcut:
                    # 단축키가 아닌 경우
                    shortcut.append(sentence[j][k])
                    if k != len(sentence[j])-1:
                        sentence[j] = sentence[j][:k] + '[' + sentence[j][k] + ']' + sentence[j][k+1:]
                    else:
                        sentence[j] = sentence[j][:k] + '[' + sentence[j][k] + ']'
                    flag = 1
                    break
                
            if flag == 1:
                break
            
    print(' '.join(sentence))