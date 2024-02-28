/*
# Question: BJ 8980 (https://www.acmicpc.net/problem/8980)
# Rank: Gold1
# Algorithm: Greedy, Sorting
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define MAX 10001
using namespace std;
typedef long long ll;
typedef pair<pair<int, int>, int> ppiii;

int N, C, M, ans=0;
vector<ppiii> v;
vector<int> truck(MAX);

bool cmp(ppiii a, ppiii b){
    return a.first.second < b.first.second;
}

void Input(){
    cin>>N>>C;
    truck.resize(C);

    cin>>M;
    for(int i=0; i<M; i++){
        int a, b, c;
        cin>>a>>b>>c;
        v.push_back({{a, b}, c});
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    sort(v.begin(), v.end(), cmp); // 도착지점을 기준으로 정렬

    for(int i=0; i<v.size(); i++){
        int start = v[i].first.first-1;
        int end = v[i].first.second-1;
        int box = v[i].second;

        int tmp = 0;
        int cnt = 0;

        for(int j=start; j<end; j++){
            tmp = max(tmp, truck[j]); // 현재 트럭에 실려있는 박스의 최대값
        }

        if(tmp + box <= C){ // C를 넘지 않은 경우
            cnt = box; 
        }else{ // C를 넘어간 경우
            cnt = C - tmp;
        }

        for(int j=start; j<end; j++){
            truck[j] += cnt; // 현재 트럭에 박스 실음
        }
        ans += cnt;
    }
    cout<<ans<<'\n';
    return 0;
}