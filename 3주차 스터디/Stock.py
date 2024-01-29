#Question : BJ 20546(https: // www.acmicpc.net/problem/20546)
#Rank : Silver5
#Algorithm : Implement, Simulation

# 준현 : BNP 전략 - 살 수 있을 때 최대한 많이 사는 전략
# 성민 : TIMING 전략 - 시간이 지나면 주가가 오르는 전략
# (3일 연속 하락장 X) -> 매수 / 그 다음날 주가 오름
# (3일 연속 상승장 X) -> 매도 / 그 다음날 주가 내림

import sys

Total=int(input())
stocks=list(map(int, sys.stdin.readline().split()))
    
def Junhyun(stocks):
    money=Total
    stock=0
    for i in range(14):
        if money >= stocks[i]:
            stock += money//stocks[i]
            money %= stocks[i]
    return money+stock*stocks[-1]

def Sungmin(stocks):
    money=Total
    stock=0
    for i in range(len(stocks)-4):
        temp=stocks[i:i+4]
        if len(temp)<4:
            continue
    
        if temp[0] < temp[1] < temp[2] < temp[3] and stock>0:
            money += (stock*temp[3])
            stock=0
        elif temp[0] > temp[1] > temp[2] > temp[3]:
            stock += (money//temp[3])
            money %= temp[3]    
    return money+stock*stocks[-1]

J=Junhyun(stocks)
S=Sungmin(stocks)

if J>S:
    print("BNP")
elif J<S:
    print("TIMING")
else:
    print("SAMESAME")
    
