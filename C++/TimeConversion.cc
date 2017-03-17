#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string time;
    cin >> time;
    char zone = time[8];
    if (zone == 'P' || zone == 'p') {
        time[0] += 1;
        int hour = time[1] - '0';
        if (hour > 7) {
            int new_hour = (hour + 2) % 10;
            time[1] = '0' + new_hour;
            time[0] += 1;
        }
        else {
            time[1] += 2;
        }
        if (time[0] == '2' && time[1] == '4') {
            time[0] = '1';
            time[1] = '2';
        }
    }
    else if ((zone == 'A' || zone == 'a') && time[0] == '1' && time[1] == '2') {
        time[0] = '0';
        time[1] = '0';
    }
    time.erase(8, 9);
    cout << time;
    return 0;
}
