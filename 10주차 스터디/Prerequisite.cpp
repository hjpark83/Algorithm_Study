/*
# Question: BJ 14567 (https://www.acmicpc.net/problem/14567)
# Rank: Gold5
# Algorithm: DP, Graph, Topological Sort, Directed Acyclic Graph
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX 1001
using namespace std;

int N, M;
vector<int> CS[MAX];
int DP[MAX];

void Input() {
    cin>>N>>M;
    for(int i=0; i<M; i++){
        int C1, C2;
        cin>>C1>>C2;
        CS[C1].push_back(C2);
    }
}

int main() {
    fastio
    Input();
    
    fill(DP+1, DP+N+1, 1);
    for(int i=1; i<=N; i++){ // 모든 과목에 대해
        for(int j=0; j<CS[i].size(); j++){ // i를 선수과목으로 가지는 과목들에 대해
            DP[CS[i][j]] = max(DP[CS[i][j]], DP[i]+1);
        }
    }
    for(int i=1; i<=N; i++){
        cout<<DP[i]<<" ";
    }

    return 0;
}