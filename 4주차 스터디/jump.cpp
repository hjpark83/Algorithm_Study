/*
# Question: BJ 1890 (https://www.acmicpc.net/problem/1890)
# Rank : Silver1
# Algorithm : DP
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 101
using namespace std;

int N;
vector<vector<int>> Map(MAX, vector<int>(MAX));
long long DP[MAX][MAX];

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>Map[i][j];
        }
    }

    DP[0][0] = 1;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(Map[i][j] == 0){
                continue;
            }
            if(i+Map[i][j]<N){
                DP[i+Map[i][j]][j] += DP[i][j];
            
            }
            if(j+Map[i][j]<N){
                DP[i][j+Map[i][j]] += DP[i][j];
            }
        }
    }
    cout << DP[N-1][N-1] << '\n';
    return 0;
}