#include <stdlib.h> // for rand()
#include "sort.h"

// ********
// ２つのデータを交換する
// ********
void swap(
    double  *a,     // データ１
    double  *b      // データ２
)
{
    double  c;

    c = *a;
    *a = *b;
    *b = c;
}

// ********
// ランダムなデータを与える
// ********
void data_random(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    int     i;

    // 0.0 <= D[i] <= 1.0 のランダムなデータ
    for( i = 0; i < n; i++ ) {
        D[i] = (double)rand() / (double)RAND_MAX;
    }
}

// ********
// 昇順のデータを与える
// ********
void data_ascending(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    int     i;

    // 0.0 <= D[i] <= 1.0 の昇順のデータ
    for( i = 0; i < n; i++ ) {
        D[i] = (double)i / (double)( n - 1 );
    }
}

// ********
// 降順のデータを与える
// ********
void data_descending(
    int     n,      // データの個数
    double  D[]     // データ D[0], ..., D[n-1]
)
{
    int     i;

    // 0.0 <= D[i] <= 1.0 の降順のデータ
    for( i = 0; i < n; i++ ) {
        D[i] = (double)( n - 1 - i ) / (double)( n - 1 );
    }
}

// **** EOF
