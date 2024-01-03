# Question: BJ 3048 (https://www.acmicpc.net/problem/3048)
# Rank : Silver 4
# Algorithm : String, Simulation

N1, N2=map(int, input().split())
A=list(input())
B=list(input())
T=int(input())

C=A[::-1]+B
for _ in range(T):
    for i in range(len(C)-1):
        if C[i] in A and C[i+1] in B:
            C[i], C[i+1]=C[i+1], C[i]
            if C[i+1] in A[0]:
                break

for i in range(N1+N2):
    print(C[i],end="")