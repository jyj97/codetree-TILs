#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int n;
    cin >> n;

    int a[100] = {};
    int cnt = -1;
    int k;
    for(int i = 0; i < n; i++){
        cin >> k;
        if(k % 2 == 0){
            a[++cnt] = k;
        }
    }

    for(int i = cnt; i >=0; i--){
        cout << a[i] << " ";
    }

    return 0;
}