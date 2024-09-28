#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int k;
    for (int i = 0; i < n; i++){
        cin >> k;
        if(k % 2 == 1 && k % 3 ==0){
            cout << k << endl;
        }
    }
    return 0;
}