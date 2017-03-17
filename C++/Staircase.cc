#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    int line = 1;
    while(line <= n) {
        string to_print = "";
        for (int temp = 0; temp < n - line; temp += 1) {
            to_print += ' ';
        }
        for (int temp2 = 0; temp2 < line; temp2 += 1) {
            to_print += '#';
        }
        cout << to_print;
        cout << "\n";
        line += 1;
    }
    return 0;
}
