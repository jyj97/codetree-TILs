#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    cin >> a >> b >> c; 
    if ((a > b && b > c) || (a < b && b < c)){
        cout << b;
    }
    else if((b > a && a > c) || (b < a && a < c)){
        cout << a;
    }
    else{
        cout << c;
    }

    return 0;
}