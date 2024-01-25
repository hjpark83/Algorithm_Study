#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, cnt;
vector<int> A; // 롤케이크의 길이가 10의 배수인 경우
vector<int> B; // 롤케이크의 길이가 10의 배수가 아닌 경우

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M;

    for(int i=0;i<N;i++){
        int cake;
        cin>>cake;
        
        if(cake<10)
            continue;
        else if(cake==10)
            cnt++;
        else if(cake%10==0)
            A.push_back(cake);
        else 
            B.push_back(cake);
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    A.insert(A.end(), B.begin(), B.end()); // A와 B를 합침

    // M개의 조각을 나눠줌
    while(M>0 && !A.empty()){
        int cake = A[0];
        int tmp = cake/10;

        if(cake%10==0){
            if(tmp-1<=M){
                cnt+=tmp;
                M-=(tmp-1);
            }else{
                cnt+=M;
                break;
            }
        }else{
            if(tmp<=M){
                cnt+=tmp;
                M-=tmp;
            }else{
                cnt+=M;
                break;
            }
        }
        A.erase(A.begin());
    }
    cout<<cnt<<"\n";
    return 0;
}