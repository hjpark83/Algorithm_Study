/*
# Question: BJ 5557 (https://www.acmicpc.net/problem/5557)
# Rank: Gold5
# Algorithm: DP
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX 101
typedef long long ll;
using namespace std;

int N;
int Num[MAX];
ll DP[MAX][MAX];

void Input() {
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>Num[i];
    }
}

int main() {
    fastio
    Input();
    
    DP[1][Num[1]] = 1;

    for(int i=2; i<=N-1; i++){
        for(int j=0; j<=20; j++){
            if(DP[i-1][j]){
                if(j+Num[i]<=20) 
                    DP[i][j+Num[i]] += DP[i-1][j];
                if(j-Num[i]>=0) 
                    DP[i][j-Num[i]] += DP[i-1][j];
            }
        }
    }
    cout<<DP[N-1][Num[N]]<<endl;
    return 0;
}