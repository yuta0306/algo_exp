#include "sort.h"

// ********
// アルゴリズム 5.2  挿入ソート
// ********
void insertionsort(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    double x;
    int j;
    for (int i = 0; i < n; i++)
    {
        x = D[i];
        j = i;
        while ((D[j - 1] > x) && (j > 0))
        {
            D[j] = D[j - 1];
            j--;
        }
        D[j] = x;
    }

}

// **** EOF
