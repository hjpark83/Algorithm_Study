/*
# Question: BJ 13335 (https://www.acmicpc.net/problem/13335)
# Rank: Silver1
# Algorithm: Implementation, Data Structure, Simulation, Queue
*/

#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define MAX 1001
using namespace std;

int N, W, L; // 다리를 건너는 트럭의 수, 다리의 길이, 다리의 최대 하중
vector<int> Truck(MAX);
queue<int> Bridge;

void Input(){
    cin>>N>>W>>L;

    Truck.resize(N);
    for(int i=0; i<N; i++){
        cin>>Truck[i];
    }
}

int main() {
    fastio;
    Input();
    
    int time=0, weight=0;
    for(int i=0; i<N; i++){
        while(true){
            if(Bridge.size()==W){ // 다리가 꽉 찼을 때 제일 앞에 있는 트럭을 뺌
                weight-=Bridge.front(); 
                Bridge.pop();
            }
            if(weight+Truck[i]<=L) // 다리에 트럭이 더 올라갈 수 있을 때
                break;
            Bridge.push(0); // 다리에 트럭이 더 올라갈 수 없을 때
            time++;
        }
        Bridge.push(Truck[i]);
        weight+=Truck[i];
        time++;
    }

    time+=W; // 마지막 트럭이 다리를 건너는 시간
    cout<<time<<'\n';
    return 0;
}