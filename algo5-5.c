#include "sort.h"
#include <stdlib.h>
#include <stdio.h>

// ********
// アルゴリズム 5.5  ヒープソート
// ********
double delete_maximum(double T[], int *size);
void push_heap(double T[], double x, int *size);

void heapsort(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    int size = 0;
    double *T = calloc(n, sizeof(double));
    if (T == NULL) exit(1);

    for (int i = 0; i < n; i++)
    {
        push_heap(T, D[i], &size);
    }
    for (int i = n-1; i >= 0; i--)
    {
        D[i] = delete_maximum(T, &size);
    }
}


double delete_maximum(double T[], int *size)
{
    int k, big;
    double max;

    if (*size > 0) {
        max = T[1];
    } else {
        return .0;
    }

    T[1] = T[*size];
    *size -= 1;
    k = 1;
    
    while (2 * k <= *size)
    {
        if (2 * k == *size) {
            if (T[k] < T[2*k]) {
                swap(&(T[k]), &(T[2*k]));
                k *= k;
            } else {
                break;
            }
        }
        else {
            if (T[2*k] > T[2*k+1]) {
                big = 2 * k;
            } else {
                big = 2*k + 1;
            }
            if (T[k] < T[big]) {
                swap(&(T[k]), &(T[big]));
                k = big;
            } else {
                break;
            }
        }
    }
    
    return max;
}
void push_heap(double T[], double x, int *size)
{
    int idx = *size = *size + 1;
    int k;
    T[idx] = x;
    k = idx;
    while ((T[k] > T[k/2]) && (k > 1))
    {
        swap(&(T[k]), &(T[k/2]));
        k /= 2;
    }
    
}

// **** EOF
