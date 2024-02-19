/*
# Question: BJ 13975 (https://www.acmicpc.net/problem/13975)
# Rank : Gold4
# Algorithm : Data Structure, Greedy, Priority Queue
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 10001
typedef long long ll;
using namespace std;

int T, K;
priority_queue<ll, vector<ll>, greater<ll>> pq;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>T;
    while(T--){
        cin>>K;

        for(int i=0; i<K; i++){
            ll fileSize;
            cin>>fileSize;
            pq.push(fileSize);
        }

        ll answer = 0;
        while(!pq.empty()){
            ll a = pq.top();
            pq.pop();

            if(pq.empty()) 
                break;
            
            ll b = pq.top();
            pq.pop();
            
            ll new_num = a+b;
            pq.push(new_num);
            answer += new_num;
        }
        cout<<answer<<'\n';
    }
    return 0;
}