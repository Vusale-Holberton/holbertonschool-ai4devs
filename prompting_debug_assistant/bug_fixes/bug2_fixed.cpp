#include <iostream>
#include <string>

using namespace std;

int main() {
    string a = "10", b = "20";
    int c = stoi(a) + stoi(b);
    int d = stoi(a) * 5;

    cout << "C-nin qiymeti: " << c << endl;
    cout << "D-nin qiymeti: " << d << endl;
    cout << "Hesablayici isleyir..." << endl;

    return 0;
}