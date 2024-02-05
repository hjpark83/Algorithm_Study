#include <iostream>
#include <vector>
using namespace std;

int LCS_LENGTH(const string& X, const string& Y) {
    int m = X.length();
    int n = Y.length();
    
    vector<vector<int>> c(m + 1, vector<int>(n + 1, 0));
    
    for (int i=1; i<=m; i++) {
        for (int j=1; j<=n; j++) {
            if (X[i-1] == Y[j-1]) {
                c[i][j] = c[i-1][j-1] + 1;
            } else if (c[i-1][j] >= c[i][j-1]) {
                c[i][j] = c[i-1][j];
            } else {
                c[i][j] = c[i][j-1];
            }
        }
    }
    
    return c[m][n];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string X, Y;
    cin >> X >> Y;

    int result = LCS_LENGTH(X, Y);
    
    cout << result << endl;
    
    return 0;
}
