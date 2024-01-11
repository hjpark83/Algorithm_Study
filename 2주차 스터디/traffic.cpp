/* 
# Question: BJ 2980 (https://www.acmicpc.net/problem/2980)
# Rank : Silver4
# Algorithm : Math, Implementation, Simulation
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N,L;
    cin>>N>>L;

    vector<vector<int>> A(N,vector<int>(3));
    vector<int> Dist(N+1);
    for(int i=0;i<N;i++){
        cin>>A[i][0]>>A[i][1]>>A[i][2];
    }

    // 신호등 사이의 거리 계산
    for(int i=0;i<=N;i++){
        if(i==0){
            Dist[i]=A[i][0];
        }else if(i==N){
            Dist[i]=L-A[i-1][0];
        }else{
            Dist[i]=A[i][0]-A[i-1][0];
        }
    }

    int total=0;
    for(int i=0;i<N;i++){
        int cycle=A[i][1]+A[i][2]; // 빨간불 + 파란불 주기
        total+=Dist[i]; // 신호등까지 이동시간
        if(A[i][1]>=(total%cycle)){
            total+=(A[i][1]-(total%cycle)); // 빨간불을 기다리는 시간
        }
    }
    total+=Dist[N]; // 마지막 신호등 없는 거리 더해주기
    cout<<total<<'\n';
    return 0;
}