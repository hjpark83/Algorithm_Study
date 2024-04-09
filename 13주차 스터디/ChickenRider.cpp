/*
# Question: BJ 15686 (https://www.acmicpc.net/problem/15686)
# Rank: Gold5
# Algorithm: Implementation, Brute-force, Backtracking
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX 51
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;

int N, M;
int ans=INF;
int City[MAX][MAX]={0,};
int Dist[MAX][MAX]={0,};
vector<pii> Chicken, House;
vector<int> idx;

void Input() {
    cin>>N>>M;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            cin>>City[i][j];
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (City[i][j] == 1)
                House.push_back({i, j});
            else if (City[i][j] == 2)
                Chicken.push_back({i, j});
        }
    }
    for (int i = 0; i < House.size(); i++){
        for (int j = 0; j < Chicken.size(); j++){
            Dist[i][j] = abs(House[i].first - Chicken[j].first) + abs(House[i].second - Chicken[j].second);
        }
    }
    for(int i=0;i<M;i++) idx.push_back(1); // M개의 치킨집을 선택
    for(int i=0;i<Chicken.size()-M;i++) idx.push_back(0); // 나머지는 폐업
    sort(idx.begin(),idx.end()); // 순열을 위한 정렬
}

int Solve() {
    do {
        int sum=0;
        for(int i=0;i<House.size();i++) {
            int minDist=INF;
            for(int j=0;j<Chicken.size();j++) {
                if(idx[j]==0) continue;
                minDist=min(minDist,Dist[i][j]);
            }
            sum+=minDist;
        }
        ans=min(ans,sum);
    } while(next_permutation(idx.begin(),idx.end()));
    
    return ans;    
}

int main() {
    fastio
    Input();
    cout<<Solve()<<'\n';
    return 0;
}