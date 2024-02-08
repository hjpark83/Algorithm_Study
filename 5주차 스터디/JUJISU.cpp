/*
# Question: BJ 15724 (https://www.acmicpc.net/problem/15724)
# Rank : Silver1
# Algorithm : DP, Aggregate Sum
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1025
using namespace std;

typedef long long ll;

int N,M,K;
ll Map[MAX][MAX];
ll DP[MAX][MAX];

void Input(){
    cin>>N>>M;
    for (int i=1; i<=N; i++){
        for (int j=1; j<=M; j++){
            cin>>Map[i][j];
        }
    }
    cin>>K;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    // 누적합
    for (int i=1; i<=N; i++){
        for (int j=1; j<=M; j++){
            DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + Map[i][j];
        }
    }

    while(K--){
        int x1, y1, x2, y2;
        cin>>x1>>y1>>x2>>y2;

        ll result = DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1];
        cout<<result<<'\n';
    }
    return 0;
}