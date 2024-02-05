/*
# Question: BJ 16928 (https://www.acmicpc.net/problem/16928)
# Rank : Gold5
# Algorithm : Graph, BFS
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<pair<int,int>> Move;
int Map[101];
int visited[101];
int N,M; // 사다리의 수, 뱀의 수
int cnt = 0;

void BFS(int start){
    queue <int> Q;
    Q.push(1);
    visited[1] = 1;
    while(!Q.empty()){
        int cur = Q.front();
        Q.pop();
        for(int i=1; i<=6; i++){
            int nx = cur + i; // 주사위 눈의 수만큼 이동
            if(nx>100 || visited[nx]!=0) // 100을 넘거나 방문했던 곳이면 continue
                continue;
            visited[nx] = visited[cur] + 1;

            if(Map[nx] != 0){
                int x = Map[nx];
                if(visited[x] != 0)
                    continue;
                visited[x] = visited[nx];
                Q.push(x);
            }else{
                Q.push(nx);
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M;
    for(int i=0;i<N+M;i++){
        int x, y;
        cin>>x>>y;
        Move.push_back({x,y});
        Map[Move[i].first] = Move[i].second; // 시작점 to 도착점
    }

    BFS(1);
    cout<<visited[100]-1<<'\n';
    return 0;
}