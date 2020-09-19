#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> S;
    for(int i = 0; i < K; ++i) {
        int l, r;
        cin >> l >> r;
        for(int j = l; j <= r; ++j) {
            S.push_back(j);
        }
    }
    vector<int> dp(N + 10);
    dp[1] = 1;
    for(int i = 1; i <= N; ++i) {
        if(dp[i] == 0) {
            continue;
        }
        for(int s : S) {
            if(i + s <= N + 1) {
                dp[i + s] = (dp[i + s] + dp[i]) % 998244353;
            }
        }
    }
    cout << dp[N] << endl;
    return 0;
}
