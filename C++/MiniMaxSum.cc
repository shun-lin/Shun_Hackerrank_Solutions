#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    long int a;
    long int b;
    long int c;
    long int d;
    long int e;
    cin >> a >> b >> c >> d >> e;
    long int raw_sum = a + b + c + d + e;
    long int min = a;
    long int max = a;
    if (min > b) {
        min = b;
    }
    if (min > c) {
        min = c;
    }
    if (min > d) {
        min = d;
    }
    if (min > e) {
        min = e;
    }
    if (max < b) {
        max = b;
    }
    if (max < c) {
        max = c;
    }
    if (max < d) {
        max = d;
    }
    if (max < e) {
        max = e;
    }
    long int without_max_sum = raw_sum - max;
    long int without_min_sum = raw_sum - min;

    cout << without_max_sum;
    cout << " ";
    cout << without_min_sum;

    return 0;
}
