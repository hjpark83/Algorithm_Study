/*
# Question: BJ 21610 (https://www.acmicpc.net/problem/21610)
# Rank: Gold5
# Algorithm: Implementation, Simulation
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MAX_N 51
#define MAX_M 101
using namespace std;
typedef pair<int, int> pii;

int N, M;
int Map[MAX_N][MAX_N];
pii dir[9] = {{0, 0}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}};
vector<pii> Cloud;
vector<pii> Command;
bool isCloud[MAX_N][MAX_N];

void Input() {
    cin>>N>>M;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin>>Map[i][j];
        }
    }
    for(int i=1; i<=M; i++){
        int d, s;
        cin>>d>>s;
        Command.push_back({d, s});
    }
}

int MakeRange(int x){
    return (x % N + N) % N;
}

bool inRange(int x, int y){
    if(x<0 || x>=N || y<0 || y>=N)
        return false;
    return true;
}
void Cloud_Exist(){
    for (int i = 0; i < Cloud.size(); i++){
        isCloud[Cloud[i].first][Cloud[i].second] = true;
    }
}

void InitCloud(){
    Cloud.push_back({N-2, 0});
    Cloud.push_back({N-2, 1});
    Cloud.push_back({N-1, 0});
    Cloud.push_back({N-1, 1});
    isCloud[N-2][0] = true;
    isCloud[N-2][1] = true;
    isCloud[N-1][0] = true;
    isCloud[N-1][1] = true;
}

void MoveCloud(int idx){
    int d = Command[idx].first;
    int s = Command[idx].second;
    memset(isCloud, false, sizeof(isCloud));
    for(int i=0; i<Cloud.size(); i++){
        int nx = Cloud[i].first;
        int ny = Cloud[i].second;
        for(int j=0; j<s; j++){
            nx += dir[d].first;
            ny += dir[d].second;
            nx = MakeRange(nx);
            ny = MakeRange(ny);
        }
        Cloud[i] = {nx, ny};
    }
    Cloud_Exist();
}

void WaterBug(){
    for(int i=0; i<Cloud.size(); i++){
        int x = Cloud[i].first;
        int y = Cloud[i].second;
        int cnt = 0;
        for(int j=2; j<=8; j+=2){
            int nx = x + dir[j].first;
            int ny = y + dir[j].second;
            if(!inRange(nx, ny)) 
                continue;
            if(Map[nx][ny] >= 1) 
                cnt++;
        }
        Map[x][y] += cnt;
    }
}

void MakeCloud(){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(isCloud[i][j] || Map[i][j]<2) 
                continue;
            Map[i][j] -= 2;
            Cloud.push_back({i, j});
        }
    }
    memset(isCloud, false, sizeof(isCloud));
    Cloud_Exist();
}

int main() {
    fastio
    Input();
    InitCloud();

    for(int i=0; i<M; i++){    
        MoveCloud(i);
        for(int j=0; j<Cloud.size(); j++){
            Map[Cloud[j].first][Cloud[j].second]++;
        }
        WaterBug();
        Cloud.clear();
        MakeCloud();
    }

    int ans = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            ans += Map[i][j];
        }
    }
    cout<<ans<<'\n';
    
    return 0;
}