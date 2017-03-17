#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* abs */
using namespace std;


int main(){
    int n;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    int a_sum = 0;
    int b_sum = 0;
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < n; j += 1) {
            if (i == j) {
                a_sum += a[i][j];
            }
            if (i + j == n - 1) {
                b_sum += a[i][j];
            }
        }
    }
    int diff = abs(a_sum - b_sum);
    cout << diff;
    return 0;
}
