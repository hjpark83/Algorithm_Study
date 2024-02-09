/*
# Question: BJ 14502 (https://www.acmicpc.net/problem/14502)
# Rank : Gold4
# Algorithm : Brute Force, Implementation, Graph, BFS
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 9
using namespace std;

int N, M, answer;
int Map[MAX][MAX];
int Temp[MAX][MAX];
int dx[] = {0,0,-1,1};
int dy[] = {-1,1,0,0};

void Input(){
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>Map[i][j];
        }
    }
}

void CopyMap(int A[MAX][MAX], int B[MAX][MAX]){
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            A[i][j] = B[i][j];
        }
    }
}

void BFS(){
    queue <pair<int,int>> Q;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(Temp[i][j]==2)
                Q.push(make_pair(i,j));
        }
    }
    while(!Q.empty()){
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx>=0 && nx<N && ny>=0 && ny<M){
                if(Temp[nx][ny] == 0){
                    Temp[nx][ny] = 2;
                    Q.push(make_pair(nx,ny));
                }
            }   
        }
    }
}

int GetSafeArea(){
    int SafeArea = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(Temp[i][j]==0)
                SafeArea++;
        }
    }
    return SafeArea;
}

void DFS(int cnt){
    if(cnt==3){
        CopyMap(Temp, Map);
        BFS();
        answer = max(answer, GetSafeArea());
        return;
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(Map[i][j] == 0){
                Map[i][j] = 1; 
                cnt++;
                DFS(cnt); 
                Map[i][j] = 0;
                cnt--;
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    DFS(0);
    cout<<answer<<'\n';
    return 0;
}