#include <iostream>
#include <string>

using namespace std;

int main() {
    string a = "100", b = "200";
    int c = stoi(a) + stoi(b);
    
    bool active_mode = true;

    cout << "Sum calculation is successful." << endl;
    cout << "Sum: " << c << endl;
    cout << "Status: " << (active_mode ? "Active" : "Inactive") << endl;
    cout << "Program reached the end safely." << endl;

    return 0;
}