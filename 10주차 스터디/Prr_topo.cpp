/*
# Question: BJ 14567 (https://www.acmicpc.net/problem/14567)
# Rank: Gold5
# Algorithm: DP, Graph, Topological Sort
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX 1001
using namespace std;

int N, M;
vector<int> adj[MAX];
int inDegree[MAX];
queue<int> Q;
int result[MAX];

void Input() {
    cin>>N>>M;
    for(int i=0; i<M; i++){
        int a, b;
        cin>>a>>b;
        adj[a].push_back(b);
        inDegree[b]++;
    }
}

void TopologicalSort(){
    for(int i=1; i<=N; i++){
        if(inDegree[i] == 0)
            Q.push(i);
        result[i] = 1;
    }

    while(!Q.empty()){
        int cur = Q.front();
        Q.pop();

        for(int i=0; i<adj[cur].size(); i++){
            int next = adj[cur][i];
            inDegree[next]--;

            if(inDegree[next] == 0){
                Q.push(next);
                result[next] = max(result[next], result[cur] + 1);
            }
        }
    }
}

int main() {
    fastio
    Input();
    TopologicalSort();

    for(int i=1; i<=N; i++){
        cout<<result[i]<<" ";
    }
    return 0;
}