#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define MAX 301
using namespace std;

int N, M, R;
int Mat[MAX][MAX];

void rotateMatrix(int startRow, int endRow, int startCol, int endCol){
    int temp = Mat[startRow][startCol];
    // 위쪽
    for (int j=startCol; j<endCol; j++){
        Mat[startRow][j] = Mat[startRow][j+1];
    }
    // 오른쪽
    for (int i=startRow; i<endRow; i++){
        Mat[i][endCol] = Mat[i+1][endCol];
    }
    // 아래쪽
    for (int j=endCol; j>startCol; j--){
        Mat[endRow][j] = Mat[endRow][j-1];
    }
    // 왼쪽
    for (int i=endRow; i>startRow; i--){
        Mat[i][startCol] = Mat[i-1][startCol];
    }
    // 기존 시작 위치의 값 저장
    Mat[startRow+1][startCol] = temp;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M>>R;

    if (min(N, M) % 2 != 0)
        return 0;

    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            cin>>Mat[i][j];
        }
    }

    int startRow=0, endRow = N-1, startCol=0, endCol = M-1;
    while (startRow<endRow && startCol<endCol){
        // 바깥쪽 테두리 회전
        for (int k=0; k<R; k++){
            rotateMatrix(startRow, endRow, startCol, endCol);
        }
        // 안쪽으로 한 칸씩 좁힘
        startRow++;
        endRow--;
        startCol++;
        endCol--;
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            cout<<Mat[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}