#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string part1 = "100";
    string part2 = "200";
    
    int total_sum = stoi(part1) + stoi(part2);
    int multiplier = stoi(part1) * 5;
    bool active_mode = true;

    cout << "Sum: " << total_sum << endl;
    cout << "Product: " << multiplier << endl;
    cout << "Status: " << (active_mode ? "Active" : "Inactive") << endl;

    return 0;
}