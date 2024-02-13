/*
# Question: BJ 5547 (https://www.acmicpc.net/problem/5547)
# Rank : Gold4
# Algorithm : Graph, BFS, DFS
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 102
using namespace std;

int W, H;
int map[MAX][MAX]={0,};

int even[6][2] = {{-1,-1}, {-1, 0}, {0, 1}, {1, 0}, {1, -1}, {0, -1}};
int odd[6][2] = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {0, -1}};

int BFS(int row, int col){
    int cnt = 0;
    queue<pair<int, int>> q;
    q.push({row, col});
    // map[row][col] = 2;

    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i=0; i<6; i++){
            int nx = x + ((x%2==0) ? even[i][0] : odd[i][0]);
            int ny = y + ((x%2==0) ? even[i][1] : odd[i][1]);
            if(nx>=0 && nx<=W+1 && ny>=0 && ny<=H+1){
                if(map[nx][ny]==0){
                    q.push({nx, ny});
                    map[nx][ny] = 2;
                }else if(map[nx][ny]==1){
                    cnt++;
                }
            }
        }
    }
    return cnt;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>H>>W;

    for (int i=1; i<=W; i++){
        for (int j=1; j<=H; j++){
            cin>>map[i][j];
        }
    }
    cout<<BFS(0,0)<<'\n';
    return 0;
}

/* 
6방향으로 탐색을 하면서 Map[i][j]==0 인 부분만 BFS로 탐색을 하는데
다음 좌표가 1인 경우 cnt를 늘려주고, 0이면 계속 탐색
끝부분이 존재하기 때문에 Map을 padding을 포함해서 만들어줘야 함
1로 막혀 있는 부분은 탐색을 하더라도 cnt를 늘리면 안됨 (어차피 (0,0)에서 시작하면 1로 막혀있는 부분은 탐색을 하지 않음)
*/