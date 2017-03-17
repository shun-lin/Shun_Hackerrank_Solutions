#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    int pos = 0;
    int neg = 0;
    int zero = 0;
    float pos_f = 0;
    float neg_f = 0;
    float zero_f = 0;
    for (int i = 0; i < n; i += 1) {
        if (arr[i] > 0) {
            pos += 1;
        }
        else if (arr[i] == 0) {
            zero += 1;
        }
        else if (arr[i] < 0) {
            neg += 1;
        }
    }
    pos_f = (float) pos / n;
    neg_f = (float) neg / n;
    zero_f = (float) zero / n;
    cout << pos_f;
    cout<<"\n";
    cout << neg_f;
    cout<<"\n";
    cout << zero_f;
    return 0;
}
