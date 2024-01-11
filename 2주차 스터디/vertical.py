# Question: BJ 10798 (https://www.acmicpc.net/problem/10798)
# Rank : Bronze 1
# Algorithm : Implementation, String

word=[[-1]*15 for i in range(5)] # 5행 15열 배열을 -1로 채움

# 입력한 string을 이차원 배열에 집어넣기
for i in range(5): # 행 만큼 반복
    str=list(input())
    for j in range(len(str)): # 한 행의 입력값 길이만큼 반복
        word[i][j]=str[j] # (행-열)로 집어넣음

# (열-행)으로 읽기
for i in range(15):
    for j in range(5):
        if word[j][i]==-1:
            continue
        else:
            print(word[j][i], end='')