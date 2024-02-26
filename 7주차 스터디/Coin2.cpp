/*
# Question: BJ 2294 (https://www.acmicpc.net/problem/2294)
# Rank : Gold5
# Algorithm : DP
*/
#include <iostream>
#include <vector>
#define MAX 10001
#define INF 1e9
using namespace std;

int N, K;
int DP[MAX];
vector<int> Coin;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>K;
    Coin.resize(N+1);

    for (int i=1; i<=N; i++){
        cin>>Coin[i];
    }

    for (int i=1; i<=K; i++){
        DP[i]=INF;
    }
    for (int i = 1; i <= N; i++){
        for (int j=Coin[i]; j<=K; j++){
            DP[j] = min(DP[j], DP[j-Coin[i]]+1);
        }
    }
    if (DP[K] == INF)
        cout<<-1<<'\n';
    else
        cout<<DP[K]<<'\n';
    return 0;
}