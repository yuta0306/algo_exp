#include "sort.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
// ********
// アルゴリズム 6.1  クイックソート
// ********

int partition(double D[], int left, int right, char base[]);

void quicksort(
    double  D[],    // データ D[left], ..., D[right]
    int     left,   // ソートの対象とする配列 D の左端の位置
    int     right,   // ソートの対象とする配列 D の右端の位置
    char    base[]
)
{   
    int pivot_index;
    if (left < right) {
        pivot_index = partition(D, left, right, base);
        quicksort(D, left, pivot_index-1, base);
        quicksort(D, pivot_index+1, right, base);
    }
}

int partition(double D[], int left, int right, char base[])
{   
    int k, i, j;
    if (strcmp(base, "left") == 0) {
        k = left;
    } else if (strcmp(base, "right") == 0) {
        k = right;
    } else if (strcmp(base, "middle") == 0) {
        k = (left+right) / 2;
    } else if (strcmp(base, "mrand") == 0) {
        double l = D[left], m = D[(left+right)/2], r = D[right];
        int mid;
        if (l < m) {
            mid = (left+right)/2;
            if (r < m) {
                mid = right;
            }
        } else {
            mid = left;
            if (r < m) {
                mid = m;
            }
        }

        k = mid;
    } else if (strcmp(base, "rand") == 0) {
        k = (double)rand() / (double)RAND_MAX * (right - left + 1);
        k = left + k;
    } else {
        k = left;
    }

    swap(&(D[k]), &(D[right]));
    i = left;
    j = right - 1;
    while (i <= j)
    {
        while (D[i] < D[right]) {
            i++;
        }
        while ((D[j] >= D[right]) && (j >= i)) {
            j--;
        }
        if (i < j) swap(&(D[i]), &(D[j]));
    }
    swap(&(D[i]), &(D[right]));

    return i;
}

// **** EOF
