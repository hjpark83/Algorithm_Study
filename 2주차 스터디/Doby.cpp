/* 
# Question: BJ 14501 (https://www.acmicpc.net/problem/14501)
# Rank : Silver3
# Algorithm : DP
*/
#include <iostream>
#include <vector>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin>>N;

    vector<int> T(N+1);
    vector<int> P(N+1);
    vector<int> DP(N+1);

    for(int i=1;i<=N;i++){
        cin>>T[i]>>P[i];
    }

    for(int i=1;i<=N;i++){
        if(i+T[i]-1<=N){
            DP[i+T[i]-1] = max(DP[i+T[i]-1], DP[i-1]+P[i]);
        }
        DP[i] = max(DP[i], DP[i-1]);
    }
    cout<<DP[N]<<'\n';
    return 0;
}