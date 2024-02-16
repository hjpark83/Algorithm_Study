/*
# Question: BJ 14728 (https://www.acmicpc.net/problem/14728)
# Rank : Gold5
# Algorithm : DP, Knapsack
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 10001
using namespace std;

int N, T, K, S;
vector<int> DP(MAX);
vector<pair<int,int>> Study;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>T;

    for(int i=0; i<N; i++){
        cin>>K>>S;
        Study.push_back({K,S});
    }

    for(int i=0; i<N; i++){
        for(int j=T; j>=Study[i].first; j--){ // T를 넘으면 안되기 때문에 T에서 시작
            DP[j] = max(DP[j], DP[j-Study[i].first] + Study[i].second);
        }
    }
    cout<<DP[T]<<'\n';
    return 0;
}