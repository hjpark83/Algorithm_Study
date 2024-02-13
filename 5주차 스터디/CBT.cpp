/*
# Question: BJ 9934 (https://www.acmicpc.net/problem/9934)
# Rank : Silver1
# Algorithm : Tree, Recursion
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define MAX 1025
using namespace std;

int K;
vector<int> arr[MAX];
vector<int> Tree(MAX);

void MakeTree(int start, int end, int level){
    if(start>end)
        return;
    
    int mid = (start+end)/2;
    arr[level].push_back(Tree[mid]); // 루트 노드

    MakeTree(start,mid-1,level+1); // 왼쪽 서브트리
    MakeTree(mid+1,end,level+1); // 오른쪽 서브트리
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>K;
    for(int i=0;i<pow(2,K)-1;i++){
        cin>>Tree[i];
    }

    MakeTree(0,pow(2,K)-2,1); // 루트 노드를 제외했기 때문에 -2

    for(int i=1; i<=K; i++){
        for(auto it:arr[i]){
            cout<<it<<" ";
        }
        cout<<'\n';
    }
}