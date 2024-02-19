/*
# Question: BJ 2688 (https://www.acmicpc.net/problem/2688)
# Rank : Silver1
# Algorithm : DP
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1001
using namespace std;

int T, N;
long long DP[10];

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>T;
    while(T--){
        cin>>N;
        fill(DP, DP+10, 1);
        for(int i=2; i<=N; i++){
            DP[1] += 1;
            for(int j=2; j<=9; j++){
                DP[j] = DP[j-1] + DP[j];
            }
        }
        long long ans = 0;
        for(int i=0; i<10; i++){
            ans += DP[i];
        }
        cout<<ans<<'\n';
    }
    return 0;
}