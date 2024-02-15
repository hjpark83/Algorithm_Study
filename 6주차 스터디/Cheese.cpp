/*
# Question: BJ 2636 (https://www.acmicpc.net/problem/2636)
# Rank : Gold4
# Algorithm : Graph, BFS, Simulation, Implementation
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 101
using namespace std;

int N, M;
int map[MAX][MAX];
int visited[MAX][MAX];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

void BFS(){
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = 1;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || nx >= N || ny < 0 || ny >= M) 
                continue;
            if(visited[nx][ny] == 0 && map[nx][ny] == 0){
                visited[nx][ny] = 1;
                q.push({nx, ny});
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M;

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> map[i][j];
        }
    }

    int time = 0;
    int cnt = 0;

    while(1){
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                visited[i][j] = 0;
            }
        }
        BFS(); // 0인 부분만 돌면서 방문처리
        int cheese = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 1){ // 바깥쪽 치즈인 경우
                    cheese++;
                    for(int k=0; k<4; k++){
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if(nx < 0 || nx >= N || ny < 0 || ny >= M) 
                            continue;
                        if(visited[nx][ny] == 1){ // 바깥쪽 치즈와 인접한 부분이 0인 경우
                            map[i][j] = 0; // 치즈가 녹음
                            break;
                        }
                    }
                }
            }
        }
        if(cheese == 0) 
            break;
        cnt = cheese;
        time++;
    }
    cout << time << "\n" << cnt << "\n";
    return 0;
}