#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    cout << fixed;
    int a = 13;
    float b = 0.165;

    cout.precision(6);
    cout << a << " * " << b << " = "<< a*b;
    return 0;
}