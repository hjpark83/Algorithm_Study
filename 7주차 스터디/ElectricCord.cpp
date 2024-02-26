/*
# Question: BJ 2565 (https://www.acmicpc.net/problem/2565)
# Rank: Gold5
# Algorithm: DP
*/

#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 501
using namespace std;
typedef pair<int, int> pii;

int N;
vector<pii> v;
vector<int> DP(MAX);

void Input(){
    cin>>N;
    DP.resize(N+1);
    for(int i=0; i<N; i++){
        int a, b;
        cin>>a>>b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    Input();
    sort(v.begin(), v.end());
    for(int i=0; i<N; i++){
        DP[i] = 1;
        for(int j=0; j<i; j++){
            if(v[i].second > v[j].second){
                DP[i] = max(DP[i], DP[j]+1);
            }
        }
    }
    int ans = 0;
    for(int i=0; i<N; i++){
        ans = max(ans, DP[i]);
    }
    cout<<N-ans<<endl;
    return 0;
}