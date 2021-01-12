#include "sort.h"
#include <stdlib.h>
#include <stdio.h>

// ********
// アルゴリズム 7.3  マージソート
// ********
void merge(double D[], int left, int mid, int right, double M[]);

void mergesort(
    double  D[],    // データ D[left], ..., D[right]
    int     left,   // ソートの対象とする配列 D の左端の位置
    int     right,   // ソートの対象とする配列 D の右端の位置
    double M[]    // コピー先の配列
)
{
    int mid = (left + right) / 2;
    if (left < mid) mergesort(D, left, mid, M);
    if (mid+1 < right) mergesort(D, mid+1, right, M);
    merge(D, left, mid, right, M);
}


void merge(double D[], int left, int mid, int right, double M[])
{
    
    int x = left;
    int y = mid + 1;
    for (int i = 0; i <= right - left; i++)
    {
        if (x == mid + 1) {
            M[i] = D[y];
            y = y + 1;
        } else if (y == right + 1) {
            M[i] = D[x];
            x = x + 1;
        } else if (D[x] <= D[y]) {
            M[i] = D[x];
            x = x + 1;
        } else {
            M[i] = D[y];
            y = y + 1;
        }
    }
    for (int i = 0; i <= right - left; i++) {
        D[left+i] = M[i];
    }
}

// **** EOF
