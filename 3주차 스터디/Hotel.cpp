/*
# Question: BJ 1106 (https://www.acmicpc.net/problem/1106)
# Rank : Gold5
# Algorithm : DP
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int C,N;
int cost, cnt;
int DP[100001];

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>C>>N;
    vector<pair<int,int>> v(N);
    for(int i=0;i<N;i++){
        cin>>cost>>cnt;
        v[i] = {cost,cnt};
    }

    for(int i=1;i<=100000;i++){
        for(int j=0;j<N;j++){
            if(i+v[j].first==0)
                DP[i] = max(DP[i], (i/v[j].first)*v[j].second);
            if(i-v[j].first >= 0)
                DP[i] = max(DP[i], DP[i-v[j].first]+v[j].second);
        }
        if(C<=DP[i]){
            cout<<i;
            return 0;
        }
    }
    return 0;
}