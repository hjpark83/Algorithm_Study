/*
# Question: BJ 9084 (https://www.acmicpc.net/problem/9084)
# Rank : Gold5
# Algorithm : DP, Knapsack
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 10001
using namespace std;

int T, N, M;
vector<int> Coin;
vector<int> DP;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>T;
    while(T--){
        cin>>N;
        Coin.resize(N+1);
        for(int i=0; i<N; i++){
            cin>>Coin[i];
        }
        cin>>M;
        DP.resize(M+1);
        DP[0]=1;
        for(int i=0; i<N; i++){
            for(int j=Coin[i]; j<=M; j++){
                DP[j]+=DP[j-Coin[i]];
            }
        }
        cout<<DP[M]<<'\n';
        Coin.clear();
        DP.clear();
    }
    return 0;
}