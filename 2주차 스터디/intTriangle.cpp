/* 
# Question: BJ 1932 (https://www.acmicpc.net/problem/1932)
# Rank : Silver1
# Algorithm : DP
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> A;
vector<vector<int>> DP;
int N;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N;

    A.resize(N,vector<int>(N,0));
    DP.resize(N,vector<int>(N,0));

    for(int i=0;i<N;i++){
        for(int j=0;j<=i;j++){
            cin>>A[i][j];
        }
    }

    int result=0;
    DP[0][0]=A[0][0];
    for(int i=1;i<N;i++){
        for(int j=0;j<=i;j++){
            if(j==0){
                DP[i][j]=DP[i-1][j]+A[i][j];
            }else if(i==j){
                DP[i][j]=DP[i-1][j-1]+A[i][j];
            }else{
                DP[i][j]=max(DP[i-1][j-1]+A[i][j],DP[i-1][j]+A[i][j]);
            }
        }
    }

    for(int i=0;i<N;i++){
        result=max(result,DP[N-1][i]);
    }
    cout<<result<<'\n';
    return 0;
}