/*
# Question: BJ 16973 (https://www.acmicpc.net/problem/16973)
# Rank : Gold4
# Algorithm : Graph, BFS, Aggregation
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 1001
using namespace std;

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

int N, M, H, W, Sr, Sc, Fr, Fc;
vector<vector<int>> Map(MAX, vector<int>(MAX, 0));
vector<vector<int>> visited(MAX, vector<int>(MAX, 0));

void Input(){
    cin >> N >> M;
    Map.resize(N, vector<int>(M, 0));
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            cin>>Map[i][j];
        }
    }
    cin >> H >> W >> Sr >> Sc >> Fr >> Fc;
}

// 직사각형 전체를 움직일 필요 없이 시작점에서 도착점까지의 거리를 구하면 됨
void BFS(int start_x, int start_y, int end_x, int end_y, int H, int W){
    queue <pair<int,int>> Q;
    Q.push({start_x, start_y});
    visited[start_x][start_y] = 1;
    while(!Q.empty()){
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();
        if(x == end_x && y == end_y){
            cout<<visited[x][y]-1<<'\n'; // 도착지점에 도착했을 때
            return;
        }
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx + H > N || ny < 0 || ny + W > M || Map[nx][ny] == 1)
                continue;

            // 직사각형의 각 꼭짓점을 검사하여 벽이 있는지 확인
            bool valid = true;
            if (i==0 || i==1){ // 위, 아래로 이동할 때
                for (int j=0; j<W; j++){
                    if (Map[nx][ny+j] == 1 || Map[nx+H-1][ny+j] == 1){
                        valid = false;
                        break;
                    }
                }
            }else{ // 좌, 우로 이동할 때
                for (int j=0; j<H; j++){
                    if (Map[nx+j][ny] == 1 || Map[nx+j][ny+W-1] == 1){
                        valid = false;
                        break;
                    }
                }
            }

            if (visited[nx][ny] == 0 && valid){
                visited[nx][ny] = visited[x][y] + 1;
                Q.push({nx, ny});
            }
        }
    }
    cout<<-1<<'\n'; // 도착지점에 도착하지 못했을 때
    return;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    BFS(Sr-1, Sc-1, Fr-1, Fc-1, H, W);
    return 0;
}